import test from "node:test";
import assert from "node:assert/strict";
import {executeBudgeted} from "./authorized-adapter.mjs";
const runId="a1234567-1234-4123-8123-123456789abc", workerId="test-worker";
const proof={provider:"openai-api",model:"test-model",requestId:"test-response",inputTokens:5,outputTokens:3,text:"synthetic"};
const setup=()=>({runId,workerId,releaseApproved:true,maxInputTokens:5,maxOutputTokens:3,
  reserve:async x=>({...x,approved:true}),provider:async()=>proof,
  rpc:async name=>name.includes("submit")?{ok:true,run_id:runId,status:"under_review",independent_supervision_required:true}:runId});
test("budget denial and mismatched grants prevent provider calls",async()=>{
  for(const override of [{approved:false},{runId:"other"},{maxOutputTokens:99}]){
    await assert.rejects(executeBudgeted({...setup(),reserve:async x=>({...x,approved:true,...override}),provider:()=>assert.fail()}),/budget_denied/);
  }
});
test("invalid allowance fails before RPC",async()=>{
  await assert.rejects(executeBudgeted({...setup(),maxInputTokens:0,rpc:()=>assert.fail()}),/invalid_budget/);
});
test("reservation precedes provider and limits are forwarded",async()=>{
  const calls=[];
  const result=await executeBudgeted({...setup(),reserve:async x=>{calls.push("reserve");return {...x,approved:true}},
    provider:async x=>{calls.push("provider");assert.equal(x.maxOutputTokens,3);return proof}});
  assert.deepEqual(calls,["reserve","provider"]);assert.equal(result.status,"under_review");
});
test("over-budget evidence never submits receipt",async()=>{
  await assert.rejects(executeBudgeted({...setup(),provider:async()=>({...proof,outputTokens:4}),
    rpc:async name=>{assert.ok(!name.includes("submit"));return runId}}),/budget_exceeded/);
});
test("ambiguous reservation does not invoke provider",async()=>{
  await assert.rejects(executeBudgeted({...setup(),reserve:async()=>{throw Error("reservation_uncertain")},provider:()=>assert.fail()}),/reservation_uncertain/);
});
