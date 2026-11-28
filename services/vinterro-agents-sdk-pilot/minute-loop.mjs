import { setTimeout as sleep } from "node:timers/promises";

// Scheduling only. A caller must supply an independently authorized and
// idempotent queue consumer. Never treats an empty tick as a completed run.
export async function runMinuteLoop({
  tick, signal, intervalMs = 60_000, maxBackoffMs = 300_000,
  delay = sleep, onEvent = () => {}
}) {
  if (typeof tick !== "function" || !signal ||
      !Number.isSafeInteger(intervalMs) || intervalMs < 15_000 ||
      !Number.isSafeInteger(maxBackoffMs) || maxBackoffMs < intervalMs) {
    throw new Error("invalid_loop_config");
  }
  let failures = 0;
  while (!signal.aborted) {
    let waitMs = intervalMs;
    try {
      await tick({ signal });
      failures = 0;
      onEvent({ kind: "tick_returned", execution_verified: false });
    } catch {
      if (signal.aborted) break;
      failures = Math.min(failures + 1, 16);
      waitMs = Math.min(maxBackoffMs, intervalMs * 2 ** (failures - 1));
      onEvent({ kind: "tick_failed", failures, retry_in_ms: waitMs });
    }
    if (signal.aborted) break;
    try { await delay(waitMs, undefined, { signal }); }
    catch (error) { if (!signal.aborted) throw error; }
  }
}
