import test from "node:test";
import assert from "node:assert/strict";
import {mkdtemp, rm} from "node:fs/promises";
import {tmpdir} from "node:os";
import {join} from "node:path";
import {createLocalReservation} from "./local-reservation.mjs";

test("persistent local reservation rejects concurrent and case-variant replay", async () => {
  const root = await mkdtemp(join(tmpdir(), "vinterro-local-"));
  try {
    const grant = {runId:"a1234567-1234-4123-8123-123456789abc",workerId:"worker-test",maxInputTokens:5,maxOutputTokens:3};
    const results = await Promise.all(Array.from({length:8}, () => createLocalReservation(root)(grant)));
    assert.equal(results.filter(x => x.approved).length, 1);
    assert.deepEqual(results.find(x => x.approved), {...grant,approved:true});
    assert.deepEqual(await createLocalReservation(root)({...grant,runId:grant.runId.toUpperCase()}), {approved:false});
    await assert.rejects(createLocalReservation(root)({...grant,runId:"../escape"}), /invalid_reservation/);
    await assert.rejects(createLocalReservation(root)({...grant,maxInputTokens:0}), /invalid_reservation/);
    await assert.rejects(createLocalReservation(join(root,"missing"))(grant), {code:"ENOENT"});
  } finally { await rm(root,{recursive:true,force:true}); }
});
