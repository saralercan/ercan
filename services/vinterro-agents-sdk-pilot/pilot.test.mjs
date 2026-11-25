import test from "node:test";
import assert from "node:assert/strict";
import { smoke } from "./pilot.mjs";

const env = { VINTERRO_SDK_ALLOW_PAID_SMOKE: "true", OPENAI_API_KEY: "test-only", OPENAI_MODEL: "test-model" };
class Agent { constructor(config) { Object.assign(this, config); } }
test("does not load SDK without explicit paid smoke opt-in", async () => {
  await assert.rejects(smoke({}, () => { throw Error("unexpected load"); }), /paid_smoke_not_enabled/);
});
test("missing credentials fail closed", async () => {
  await assert.rejects(smoke({ ...env, OPENAI_API_KEY: "" }), /openai_key_missing/);
});
test("synthetic handoff verified and never marked production execution", async () => {
  const result = await smoke(env, async () => ({ Agent, run: async (agent, nonce, options) => {
    assert.equal(options.maxTurns, 3);
    assert.equal(agent.handoffs.length, 1);
    assert.equal(agent.tools, undefined);
    return { finalOutput: nonce, lastAgent: agent.handoffs[0], lastResponseId: "resp_mock_only", state: { usage: {requests:2,inputTokens:12,outputTokens:5} } };
  }}));
  assert.equal(result.status, "passed");
  assert.equal(result.production_execution, false);
  assert.equal(result.provider_request_id,"resp_mock_only");
  assert.equal(result.requests,2);
});
test("a fabricated or wrong final answer fails closed", async () => {
  await assert.rejects(smoke(env, async () => ({ Agent, run: async (agent) => ({
    finalOutput: "wrong", lastAgent: agent.handoffs[0]
  }) })), /handoff_or_output_not_verified/);
});

test("matching output without provider evidence fails closed", async () => {
  await assert.rejects(smoke(env, async () => ({ Agent, run: async (agent, nonce) => ({
    finalOutput: nonce, lastAgent: agent.handoffs[0]
  }) })), /provider_evidence_missing/);
});
test("single request cannot prove a two-agent handoff", async () => {
  await assert.rejects(smoke(env, async () => ({ Agent, run: async (agent, nonce) => ({
    finalOutput: nonce, lastAgent: agent.handoffs[0], lastResponseId:"resp_mock",
    state:{usage:{requests:1,inputTokens:5,outputTokens:3}}
  }) })), /provider_evidence_missing/);
});
