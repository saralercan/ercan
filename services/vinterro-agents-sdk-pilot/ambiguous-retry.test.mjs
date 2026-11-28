import test from "node:test";
import assert from "node:assert/strict";
import { executeBudgeted } from "./authorized-adapter.mjs";

for (const failure of ["provider", "receipt"]) {
  test("ambiguous " + failure + " failure retains reservation across retry", async () => {
    const runId = "a1234567-1234-4123-8123-123456789abc";
    const reservations = new Set();
    let providerCalls = 0, receiptCalls = 0;
    const options = {
      runId, workerId: "test-worker", releaseApproved: true,
      maxInputTokens: 5, maxOutputTokens: 3,
      reserve: async grant => {
        if (reservations.has(grant.runId)) return { approved: false };
        reservations.add(grant.runId);
        return { ...grant, approved: true };
      },
      rpc: async name => {
        if (name.includes("submit")) {
          receiptCalls++;
          throw Error("receipt_uncertain");
        }
        return runId;
      },
      provider: async () => {
        providerCalls++;
        if (failure === "provider") throw Error("provider_uncertain");
        return {provider:"openai-api",model:"test-model",requestId:"test-response",
          inputTokens:5,outputTokens:3,text:"synthetic"};
      }
    };
    await assert.rejects(executeBudgeted(options), new RegExp(failure + "_uncertain"));
    await assert.rejects(executeBudgeted({...options,workerId:"other-worker"}), /budget_denied/);
    assert.equal(providerCalls, 1);
    assert.equal(receiptCalls, failure === "receipt" ? 1 : 0);
    assert.equal(reservations.size, 1);
  });
}
