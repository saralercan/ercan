import test from "node:test";
import assert from "node:assert/strict";
import { mkdtemp, rm, mkdir } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { executeBudgeted } from "./authorized-adapter.mjs";

// Filesystem-backed reservation double: atomic directory creation survives
// adapter recreation. Test-only; never use this as a distributed backend.
test("durable reservation double prevents replay after adapter recreation", async () => {
  const root = await mkdtemp(join(tmpdir(), "vinterro-reservation-"));
  try {
    const runId = "a1234567-1234-4123-8123-123456789abc";
    let calls = 0;
    const makeOptions = () => ({
      runId, workerId: "worker-test", releaseApproved: true,
      maxInputTokens: 5, maxOutputTokens: 3,
      reserve: async grant => {
        try { await mkdir(join(root, grant.runId)); }
        catch (error) {
          if (error.code === "EEXIST") return { approved: false };
          throw error;
        }
        return { ...grant, approved: true };
      },
      rpc: async name => {
        if (name.includes("submit")) throw Error("unexpected_receipt");
        return runId;
      },
      provider: async () => { calls++; throw Error("ambiguous_provider"); }
    });
    await assert.rejects(executeBudgeted(makeOptions()), /ambiguous_provider/);
    await assert.rejects(executeBudgeted(makeOptions()), /budget_denied/);
    assert.equal(calls, 1);
  } finally { await rm(root, { recursive: true, force: true }); }
});
