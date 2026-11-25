import test from "node:test";
import assert from "node:assert/strict";
import { runMinuteLoop } from "./minute-loop.mjs";

test("one minute cadence, never concurrent, no completion claims", async () => {
  const controller = new AbortController();
  const waits = [], events = [];
  let calls = 0, active = 0;
  await runMinuteLoop({
    signal: controller.signal,
    tick: async () => { assert.equal(++active, 1); calls++; await Promise.resolve(); active--; },
    delay: async ms => { waits.push(ms); if (calls === 3) controller.abort(); },
    onEvent: event => events.push(event)
  });
  assert.equal(calls, 3);
  assert.deepEqual(waits, [60000,60000,60000]);
  assert.ok(events.every(e => e.execution_verified === false));
});
test("bounded backoff resets after recovery", async () => {
  const controller = new AbortController();
  const waits = [];
  let calls = 0;
  await runMinuteLoop({
    signal: controller.signal,
    tick: async () => { if (++calls < 5) throw Error("transient"); },
    delay: async ms => { waits.push(ms); if(calls === 5) controller.abort(); }
  });
  assert.deepEqual(waits, [60000,120000,240000,300000,60000]);
});
test("rejects unsafe loop configuration", async () => {
  await assert.rejects(runMinuteLoop({ tick: async()=>{}, signal: new AbortController().signal, intervalMs: 0 }), /invalid_loop_config/);
});
