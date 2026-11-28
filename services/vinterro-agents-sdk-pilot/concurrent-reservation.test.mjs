import test from "node:test";
import assert from "node:assert/strict";
import { mkdtemp, mkdir, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { executeBudgeted } from "./authorized-adapter.mjs";

test("concurrent workers cannot both invoke provider for one reserved run", async () => {
  const root = await mkdtemp(join(tmpdir(), "vinterro-contention-"));
  try {
    const runId = "a1234567-1234-4123-8123-123456789abc";
    let calls = 0;
    const reserve = async grant => {
      try { await mkdir(join(root, grant.runId)); }
      catch (error) {
        if (error.code === "EEXIST") return {approved:false};
        throw error;
      }
      return {...grant, approved:true};
    };
    const outcomes = await Promise.allSettled(Array.from({length: 8}, (_, i) =>
      executeBudgeted({
        runId, workerId: "worker-" + i, releaseApproved:true,
        maxInputTokens:5, maxOutputTokens:3, reserve,
        rpc: async name => {
          if (name.includes("submit")) throw Error("unexpected_receipt");
          return runId;
        },
        provider: async () => { calls++; throw Error("ambiguous_provider"); }
      })
    ));
    assert.equal(calls, 1);
    assert.equal(outcomes.filter(x => x.status === "rejected" && x.reason.message === "budget_denied").length, 7);
    assert.equal(outcomes.filter(x => x.status === "rejected" && x.reason.message === "ambiguous_provider").length, 1);
  } finally { await rm(root, {recursive:true, force:true}); }
});
