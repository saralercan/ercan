import { randomUUID } from "node:crypto";
import { pathToFileURL } from "node:url";

export function assertConfig(env) {
  if (env.VINTERRO_SDK_ALLOW_PAID_SMOKE !== "true") throw new Error("paid_smoke_not_enabled");
  if (!env.OPENAI_API_KEY?.trim()) throw new Error("openai_key_missing");
  if (!env.OPENAI_MODEL?.trim()) throw new Error("openai_model_missing");
}

export function extractEvidence(result) {
  const id = result.lastResponseId;
  const usage = result.state?.usage ?? result.runContext?.usage;
  if (typeof id !== "string" || !id.startsWith("resp_") || id.length > 256 ||
      !Number.isSafeInteger(usage?.requests) || usage.requests < 2 || usage.requests > 3 ||
      !Number.isSafeInteger(usage.inputTokens) || usage.inputTokens <= 0 ||
      !Number.isSafeInteger(usage.outputTokens) || usage.outputTokens <= 0) {
    throw new Error("provider_evidence_missing");
  }
  return { provider_request_id: id, requests: usage.requests,
    input_tokens: usage.inputTokens, output_tokens: usage.outputTokens };
}

export async function smoke(env = process.env, loadSdk = () => import("@openai/agents")) {
  assertConfig(env);
  const { Agent, run } = await loadSdk();
  const nonce = randomUUID();
  const started = Date.now();
  const reviewer = new Agent({
    name: "PilotReviewer",
    model: env.OPENAI_MODEL,
    modelSettings: { maxTokens: 256 },
    instructions: "Synthetic QA only. Return the provided nonce exactly, without commentary. Never access external systems.",
  });
  const coordinator = new Agent({
    name: "PilotCoordinator",
    model: env.OPENAI_MODEL,
    modelSettings: { maxTokens: 256 },
    instructions: "Immediately hand off the synthetic nonce to PilotReviewer. Do not answer yourself.",
    handoffs: [reviewer],
  });
  const result = await run(coordinator, nonce, { maxTurns: 3, signal: AbortSignal.timeout(60_000) });
  if (result.lastAgent?.name !== "PilotReviewer" || result.finalOutput?.trim() !== nonce) {
    throw new Error("handoff_or_output_not_verified");
  }
  return {
    kind: "synthetic_sdk_smoke",
    ...extractEvidence(result),
    status: "passed",
    run_id: nonce,
    final_agent: result.lastAgent.name,
    model: env.OPENAI_MODEL,
    latency_ms: Date.now() - started,
    production_execution: false,
  };
}

if (process.argv[1] && import.meta.url === pathToFileURL(process.argv[1]).href) {
  try {
    console.log(JSON.stringify(await smoke()));
  } catch (error) {
    // Never log raw provider errors or secrets.
    const safeCodes = new Set(["paid_smoke_not_enabled", "openai_key_missing", "openai_model_missing", "handoff_or_output_not_verified", "provider_evidence_missing"]);
    console.error(JSON.stringify({ status: "blocked", reason: safeCodes.has(error?.message) ? error.message : "sdk_or_provider_error", provider_status: Number.isInteger(error?.status) ? error.status : undefined }));
    process.exitCode = 1;
  }
}
