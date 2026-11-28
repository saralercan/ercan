import test from "node:test";
import assert from "node:assert/strict";
import {mkdtemp,rm} from "node:fs/promises";
import {tmpdir} from "node:os";
import {join} from "node:path";
import {createAggregateReservation} from "./aggregate-reservation.mjs";

test("aggregate cap and duplicate denial persist across independent connections and restart", async()=>{
  const root=await mkdtemp(join(tmpdir(),"pilot-ledger-"));
  const path=join(root,"budget.sqlite");
  const handles=[];
  const open=cap=>{const h=createAggregateReservation(path,cap);handles.push(h);return h;};
  const grant=(n)=>({runId:`${String(n).padStart(8,"0")}-1111-4111-8111-111111111111`,workerId:"worker-a",maxInputTokens:60,maxOutputTokens:40});
  try {
    const a=open(250),b=open(250);
    const results=await Promise.all([a.reserve(grant(1)),b.reserve(grant(2)),a.reserve(grant(3))]);
    assert.equal(results.filter(x=>x.approved).length,2);
    assert.equal((await b.reserve(grant(1))).approved,false);
    assert.throws(()=>createAggregateReservation(path,500),/budget_config_mismatch/);
    while(handles.length) handles.pop().close();
    const c=open(250);
    assert.equal((await c.reserve(grant(4))).approved,false);
    assert.equal((await c.reserve({...grant(4),maxInputTokens:30,maxOutputTokens:20})).approved,true);
    assert.equal((await c.reserve({...grant(5),maxInputTokens:1,maxOutputTokens:1})).approved,false);
  } finally {while(handles.length) handles.pop().close();await rm(root,{recursive:true,force:true});}
});
