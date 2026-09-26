import test from "node:test";
import assert from "node:assert/strict";

test("worker source keeps the control-plane contract explicit", async () => {
  process.env.SUPABASE_URL = process.env.SUPABASE_URL || "https://example.supabase.co";
  process.env.VINTERRO_SALES_WORKER_TOKEN = process.env.VINTERRO_SALES_WORKER_TOKEN || "test-token";
  const source = await import("./worker.mjs?test-contract");
  assert.equal(typeof source.configOk, "function");
  assert.equal(typeof source.runTick, "function");
});
