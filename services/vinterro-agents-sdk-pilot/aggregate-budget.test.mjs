import test from "node:test";
import assert from "node:assert/strict";
import { mkdtemp, rm } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { createLocalReservation } from "./local-reservation.mjs";

// Characterization of the single-host pilot: distinct runs are not subject
// to a shared spending cap. Keep this limitation explicit until a ledger
// with atomic aggregate accounting is introduced.
test("local reservation is per run, not an aggregate budget ledger", async () => {
  const root = await mkdtemp(join(tmpdir(), "pilot-budget-"));
  try {
    const reserve = createLocalReservation(root);
    const common = {workerId:"worker-a", maxInputTokens:100, maxOutputTokens:100};
    const grants = await Promise.all([
      reserve({...common,runId:"11111111-1111-4111-8111-111111111111"}),
      reserve({...common,runId:"22222222-2222-4222-8222-222222222222"})
    ]);
    assert.equal(grants.filter(g => g.approved).length, 2);
    assert.equal(grants.reduce((n,g)=>n+g.maxInputTokens+g.maxOutputTokens,0),400);
  } finally { await rm(root,{recursive:true,force:true}); }
});
