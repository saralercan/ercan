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

import { createHash } from "node:crypto";
import { executeSignedBudgeted } from "./authorized-adapter.mjs";

test("signed budgeted adapter submits only authentic output for the claimed run", async () => {
  const {publicKey, privateKey} = generateKeyPairSync("ed25519");
  const runId="a1234567-1234-4123-8123-123456789abc", workerId="test-worker";
  const proof={provider:"openai-api",model:"test-model",requestId:"test-response",inputTokens:5,outputTokens:3,text:"synthetic"};
  const evidence={runId,workerId,requestId:proof.requestId,outputSha256:createHash("sha256").update(proof.text).digest("hex")};
  const signature=sign(null,Buffer.from(JSON.stringify(["vinterro-receipt-v1",...Object.values(evidence)])),privateKey).toString("base64url");
  const signed={...proof,evidence,signature};
  for(const [result, valid] of [[signed,true],[{...signed,text:"tampered"},false],[{...signed,requestId:"other-request"},false],[{...signed,signature:"A".repeat(86)},false],[{...signed,signature:undefined},false]]) {
    const receipts=[];
    const pending=executeSignedBudgeted({runId,workerId,publicKey,releaseApproved:true,maxInputTokens:5,maxOutputTokens:3,
      reserve:async x=>({...x,approved:true}),provider:async()=>result,
      rpc:async (name,args)=>{
        if(name.includes("submit")) {
          receipts.push(args);
          return {ok:true,run_id:runId,status:"under_review",independent_supervision_required:true};
        }
        return runId;
      }});
    if(valid) {
      assert.equal((await pending).status,"under_review");
      assert.equal(receipts.length,1);
      assert.equal(receipts[0].p_output_text,proof.text);
    } else {
      await assert.rejects(pending,/invalid_signed_evidence/);
      assert.equal(receipts.length,0);
    }
  }
});
