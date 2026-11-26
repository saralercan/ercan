import test from "node:test";
import assert from "node:assert/strict";
import { executeAuthorized } from "./authorized-adapter.mjs";
const runId="a1234567-1234-4123-8123-123456789abc";
const workerId="test-worker";
const proof={provider:"openai-api",model:"test-model",requestId:"test-response",inputTokens:5,outputTokens:3,text:"synthetic"};
test("closed release gate performs no calls",async()=>{
  await assert.rejects(executeAuthorized({runId,workerId,rpc:()=>assert.fail(),provider:()=>assert.fail()}),/release_gate_closed/);
});
test("unclaimable job never invokes model",async()=>{
  const calls=[];
  const out=await executeAuthorized({runId,workerId,releaseApproved:true,rpc:async(name)=>{calls.push(name);return null},provider:()=>assert.fail()});
  assert.deepEqual(calls,["vinterro_agent_worker_heartbeat","vinterro_agent_claim_authorized_run"]);
  assert.equal(out.status,"not_claimable");
});
test("valid receipt remains under review",async()=>{
  const calls=[];
  const out=await executeAuthorized({runId,workerId,releaseApproved:true,provider:async()=>proof,rpc:async(name,args)=>{
    calls.push(name); if(name.includes("claim"))return runId;
    if(name.includes("submit")) {assert.equal(args.p_provider_request_id,proof.requestId);return {ok:true,run_id:runId,status:"under_review",independent_supervision_required:true}}
  }});
  assert.equal(out.status,"under_review");assert.equal(out.execution_verified,false);assert.equal(calls.length,3);
});
test("invalid evidence cannot submit a receipt",async()=>{
  const calls=[];
  await assert.rejects(executeAuthorized({runId,workerId,releaseApproved:true,provider:async()=>({...proof,requestId:""}),rpc:async(name)=>{calls.push(name);return runId}}),/invalid_provider_evidence/);
  assert.equal(calls.length,2);
});
test("uncertain receipt is not retried or marked successful",async()=>{
  const calls=[];
  await assert.rejects(executeAuthorized({runId,workerId,releaseApproved:true,provider:async()=>proof,rpc:async(name)=>{calls.push(name);return name.includes("claim")?runId:null}}),/receipt_unverified/);
  assert.equal(calls.length,3);
});


test("mismatched claim never invokes provider or submits receipt", async()=>{
  const calls=[];
  await assert.rejects(executeAuthorized({runId,workerId,releaseApproved:true,
    provider:()=>assert.fail("provider must not run"),
    rpc:async(name)=>{calls.push(name);return "b1234567-1234-4123-8123-123456789abc"}}),/claim_mismatch/);
  assert.deepEqual(calls,["vinterro_agent_worker_heartbeat","vinterro_agent_claim_authorized_run"]);
});
test("provider failure never retries or submits receipt", async()=>{
  const calls=[]; let attempts=0;
  await assert.rejects(executeAuthorized({runId,workerId,releaseApproved:true,
    provider:async()=>{attempts++;throw Error("ambiguous_provider_failure")},
    rpc:async(name)=>{calls.push(name);return runId}}),/ambiguous_provider_failure/);
  assert.equal(attempts,1);
  assert.equal(calls.length,2);
});
test("receipt transport failure never retries provider or receipt", async()=>{
  const calls=[]; let attempts=0;
  await assert.rejects(executeAuthorized({runId,workerId,releaseApproved:true,
    provider:async()=>{attempts++;return proof},
    rpc:async(name)=>{calls.push(name);if(name.includes("submit"))throw Error("ambiguous_receipt_failure");return runId}}),/ambiguous_receipt_failure/);
  assert.equal(attempts,1);
  assert.equal(calls.length,3);
});
