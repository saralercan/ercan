import test from "node:test";
import assert from "node:assert/strict";
import { generateKeyPairSync, sign, createHash } from "node:crypto";
import { executeSignedBudgeted } from "./authorized-adapter.mjs";

// Characterize the v1 signature coverage without touching a real provider or queue.
// A future version must reject these mutations; this test records the current gap.
test("v1 receipt does not authenticate model or token accounting", async () => {
  const { publicKey, privateKey } = generateKeyPairSync("ed25519");
  const runId = "a1234567-1234-4123-8123-123456789abc", workerId = "test-worker";
  const proof = { provider: "openai-api", model: "test-model", requestId: "test-response",
    inputTokens: 5, outputTokens: 3, text: "synthetic" };
  const evidence = { runId, workerId, requestId: proof.requestId,
    outputSha256: createHash("sha256").update(proof.text).digest("hex") };
  const signature = sign(null, Buffer.from(JSON.stringify(["vinterro-receipt-v1",
    runId, workerId, proof.requestId, evidence.outputSha256])), privateKey).toString("base64url");
  for (const mutation of [{ model: "other-model" }, { inputTokens: 4 }, { outputTokens: 2 }]) {
    const receipts = [];
    const result = await executeSignedBudgeted({ runId, workerId, publicKey, releaseApproved: true,
      maxInputTokens: 5, maxOutputTokens: 3, reserve: async x => ({ ...x, approved: true }),
      provider: async () => ({ ...proof, ...mutation, evidence, signature }),
      rpc: async (name, args) => {
        if (name.includes("submit")) {
          receipts.push(args);
          return { ok: true, run_id: runId, status: "under_review", independent_supervision_required: true };
        }
        return runId;
      } });
    assert.equal(result.status, "under_review");
    assert.equal(receipts.length, 1);
    const [field, value] = Object.entries(mutation)[0];
    assert.equal(receipts[0][{ model: "p_model", inputTokens: "p_input_tokens", outputTokens: "p_output_tokens" }[field]], value);
  }
});
