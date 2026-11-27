import test from "node:test";
import assert from "node:assert/strict";
import {mkdtemp,rm} from "node:fs/promises";
import {tmpdir} from "node:os";
import {join} from "node:path";
import {Worker} from "node:worker_threads";

test("aggregate ledger enforces cap across actual concurrent worker threads", async()=>{
  const root=await mkdtemp(join(tmpdir(),"pilot-parallel-"));
  const path=join(root,"budget.sqlite");
  const workers=[];
  const gate=new SharedArrayBuffer(4);
  const moduleUrl=new URL("./aggregate-reservation.mjs",import.meta.url).href;
  try {
    const jobs=Array.from({length:8},(_,i)=>new Promise((resolve,reject)=>{
      const worker=new Worker(`
        const {parentPort,workerData}=require("node:worker_threads");
        (async()=>{
          const {createAggregateReservation}=await import(workerData.moduleUrl);
          const ledger=createAggregateReservation(workerData.path,300);
          try {
            parentPort.postMessage("ready");
            Atomics.wait(new Int32Array(workerData.gate),0,0,10000);
            const result=await ledger.reserve({runId:workerData.id,workerId:"worker-a",maxInputTokens:60,maxOutputTokens:40});
            parentPort.postMessage(result.approved);
          } finally {ledger.close();}
        })().catch(e=>{throw e;});
      `,{eval:true,workerData:{moduleUrl,path,gate,id:`${String(i).padStart(8,"0")}-1111-4111-8111-111111111111`}});
      workers.push(worker);
      worker.on("message",value=>{
        if(value==="ready"){
          ready++;
          if(ready===8){Atomics.store(new Int32Array(gate),0,1);Atomics.notify(new Int32Array(gate),0);}
        } else resolve(value);
      });
      worker.on("error",reject);
      worker.on("exit",code=>{if(code!==0)reject(Error("worker_exit_"+code));});
    }));
    var ready=0;
    const results=await Promise.all(jobs);
    assert.equal(results.filter(x=>x===true).length,3);
    assert.equal(results.filter(x=>x===false).length,5);
  } finally {
    await Promise.all(workers.map(w=>w.terminate()));
    await rm(root,{recursive:true,force:true});
  }
});
