// Explicit, pre-authorized single-run adapter. No queue scan or release bypass.
// The caller must provide authenticated backend RPC and a separately approved
// provider implementation. A receipt means under_review, never completed.
const UUID = /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i;
export async function executeAuthorized({runId, workerId, rpc, provider, releaseApproved=false}) {
  if (releaseApproved !== true) throw Error("release_gate_closed");
  if (typeof runId !== "string" || typeof workerId !== "string" ||
      !UUID.test(runId) || !/^[a-z0-9_.-]{3,128}$/i.test(workerId) ||
      typeof rpc !== "function" || typeof provider !== "function") throw Error("invalid_config");
  await rpc("vinterro_agent_worker_heartbeat", {p_worker_id: workerId});
  const claimed = await rpc("vinterro_agent_claim_authorized_run",{p_run_id:runId,p_worker_id:workerId});
  if (claimed === null) return {status:"not_claimable",execution_verified:false};
  if (claimed !== runId) throw Error("claim_mismatch");
  // No retry after an ambiguous provider/receipt response. The operator must
  // reconcile the claimed run against the immutable receipt before any retry.
  const p = await provider({runId,workerId});
  if (p?.provider !== "openai-api" || typeof p.model !== "string" || p.model.trim().length < 2 ||
      typeof p.requestId !== "string" || p.requestId.trim().length < 3 ||
      !Number.isSafeInteger(p.inputTokens) || p.inputTokens < 0 ||
      !Number.isSafeInteger(p.outputTokens) || p.outputTokens < 0 ||
      !Number.isSafeInteger(p.inputTokens+p.outputTokens) || p.inputTokens+p.outputTokens <= 0 ||
      typeof p.text !== "string" || !p.text.trim() || p.text.length>16000) throw Error("invalid_provider_evidence");
  const receipt = await rpc("vinterro_agent_submit_provider_result",{
    p_run_id:runId,p_worker_id:workerId,p_provider:p.provider,p_model:p.model,
    p_provider_request_id:p.requestId,p_input_tokens:p.inputTokens,p_output_tokens:p.outputTokens,p_output_text:p.text
  });
  if (receipt?.ok !== true || receipt.run_id !== runId || receipt.status !== "under_review" ||
      receipt.independent_supervision_required !== true) throw Error("receipt_unverified");
  return {status:"under_review",execution_verified:false,receipt_recorded:true};
}
