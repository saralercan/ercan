import test from "node:test";
import assert from "node:assert/strict";
import { executeBudgeted } from "./authorized-adapter.mjs";

test("shared atomic reservation double blocks concurrent duplicate runs", async () => {
  const runId = "a1234567-1234-4123-8123-123456789abc";
  const reserved = new Set();
  let providerCalls = 0, receipts = 0;
  const options = {
    runId, releaseApproved: true, maxInputTokens: 5, maxOutputTokens: 3,
    reserve: async grant => {
      if (reserved.has(grant.runId)) return { approved: false };
      reserved.add(grant.runId);
      return { ...grant, approved: true };
    },
    rpc: async name => {
      if (name.includes("submit")) {
        receipts++;
        return { ok: true, run_id: runId, status: "under_review", independent_supervision_required: true };
      }
      return runId;
    },
    provider: async () => {
      providerCalls++;
      return { provider: "openai-api", model: "test-model", requestId: "test-response", inputTokens: 5, outputTokens: 3, text: "synthetic" };
    }
  };
  const results = await Promise.allSettled([
    executeBudgeted({ ...options, workerId: "worker-one" }),
    executeBudgeted({ ...options, workerId: "worker-two" })
  ]);
  assert.equal(results.filter(r => r.status === "fulfilled").length, 1);
  assert.match(results.find(r => r.status === "rejected").reason.message, /budget_denied/);
  assert.equal(providerCalls, 1);
  assert.equal(receipts, 1);
  await assert.rejects(executeBudgeted({ ...options, workerId: "worker-three" }), /budget_denied/);
  assert.equal(providerCalls, 1);
});
