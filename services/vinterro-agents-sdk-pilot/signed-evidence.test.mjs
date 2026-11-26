import test from "node:test";
import assert from "node:assert/strict";
import { generateKeyPairSync, sign } from "node:crypto";
import { verifySignedEvidence } from "./signed-evidence.mjs";
test("receipt signature binds run, worker, request and output digest", () => {
  const {publicKey, privateKey} = generateKeyPairSync("ed25519");
  const evidence = {runId:"synthetic-run",workerId:"worker-one",requestId:"request-one",outputSha256:"a".repeat(64)};
  const signature = sign(null, Buffer.from(JSON.stringify(["vinterro-receipt-v1",...Object.values(evidence)])), privateKey).toString("base64url");
  const args = {evidence,signature,publicKey,expected:{...evidence}};
  assert.equal(verifySignedEvidence(args),true);
  for (const field of Object.keys(evidence)) {
    const changed = {...evidence,[field]:field==="outputSha256"?"b".repeat(64):"changed"};
    assert.equal(verifySignedEvidence({...args,evidence:changed,expected:changed}),false);
    assert.equal(verifySignedEvidence({...args,expected:changed}),false);
  }
  assert.equal(verifySignedEvidence({...args,publicKey:generateKeyPairSync("ed25519").publicKey}),false);
  assert.equal(verifySignedEvidence({...args,signature:signature+"="}),false);
  assert.equal(verifySignedEvidence({...args,publicKey:null}),false);
});
