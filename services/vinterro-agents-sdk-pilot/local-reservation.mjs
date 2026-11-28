import { mkdir } from "node:fs/promises";
import { join, isAbsolute } from "node:path";

// Isolated single-host pilot only. Pre-provision a private persistent directory.
// One atomic directory per run; never refund or remove on ambiguous failure.
// Not a distributed budget ledger or an aggregate spending cap.
export function createLocalReservation(root) {
  if (typeof root !== "string" || !isAbsolute(root)) throw Error("invalid_reservation_root");
  return async grant => {
    const {runId, workerId, maxInputTokens, maxOutputTokens} = grant ?? {};
    if (typeof runId !== "string" || !/^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(runId) ||
        typeof workerId !== "string" || !/^[a-z0-9_.-]{3,128}$/i.test(workerId) ||
        !Number.isSafeInteger(maxInputTokens) || maxInputTokens <= 0 ||
        !Number.isSafeInteger(maxOutputTokens) || maxOutputTokens <= 0 ||
        !Number.isSafeInteger(maxInputTokens + maxOutputTokens)) throw Error("invalid_reservation");
    try { await mkdir(join(root, runId.toLowerCase()), {mode:0o700}); }
    catch (error) {
      if (error.code === "EEXIST") return {approved:false};
      throw error;
    }
    return {runId, workerId, maxInputTokens, maxOutputTokens, approved:true};
  };
}
