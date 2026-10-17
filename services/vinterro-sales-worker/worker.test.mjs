import test from "node:test";
import assert from "node:assert/strict";

test("worker source keeps the control-plane contract explicit", async () => {
  process.env.SUPABASE_URL = process.env.SUPABASE_URL || "https://example.supabase.co";
  process.env.VINTERRO_SALES_WORKER_TOKEN = process.env.VINTERRO_SALES_WORKER_TOKEN || "test-token";
  const source = await import("./worker.mjs?test-contract");
  assert.equal(typeof source.configOk, "function");
  assert.equal(typeof source.runTick, "function");
});


test("worker is passive by default and refuses ticks without a trusted user command", async () => {
  process.env.SUPABASE_URL = "https://example.supabase.co";
  process.env.VINTERRO_SALES_WORKER_TOKEN = "test-token";
  const worker = await import("./worker.mjs?manual-only");
  let outgoing = 0;
  const fakeFetch = async () => { outgoing += 1; return { ok: true, json: async () => ({ ok: true }) }; };
  await assert.rejects(worker.runTick(fakeFetch), /explicit_operator_command_required/);
  await assert.rejects(worker.runTick(fakeFetch, { origin: "scheduler" }), /explicit_operator_command_required/);
  assert.equal(outgoing, 0);
  const now = Date.now();
  const command = {
    origin: "authenticated_user", verifiedByTrustedBoundary: true, replayProtectionConfirmed: true,
    userId: "operator-1", commandId: "cmd-20261011-1", action: "vinterro.sales.tick",
    issuedAt: new Date(now - 1000).toISOString(), expiresAt: new Date(now + 60000).toISOString()
  };
  await worker.runTick(fakeFetch, command);
  assert.equal(outgoing, 1);
  assert.equal(worker.hasOperatorCommand({ ...command, action: "send_email" }), false);
  assert.equal(worker.hasOperatorCommand({ ...command, expiresAt: new Date(now - 1000).toISOString() }), false);
});

test("worker source must not schedule recurring or boot-time dispatch", async () => {
  const { readFile } = await import("node:fs/promises");
  const source = await readFile(new URL("./worker.mjs", import.meta.url), "utf8");
  assert.doesNotMatch(source, /setInterval\s*\(/);
  assert.doesNotMatch(source, /void tickSafely\s*\(/);
});
