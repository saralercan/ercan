// Bounded infrastructure test: no credentials, model calls or live queue access.
import { Agent } from "@openai/agents";
import { runMinuteLoop } from "./minute-loop.mjs";
const controller = new AbortController();
const started = Date.now();
let ticks = 0;
process.once("SIGTERM", () => controller.abort());
process.once("SIGINT", () => controller.abort());
const deadline = setTimeout(() => controller.abort(), 185_000);
try {
  await runMinuteLoop({
    signal: controller.signal,
    tick: async () => {
      const reviewer = new Agent({name:"StagingReviewer",instructions:"Synthetic only"});
      new Agent({name:"StagingCoordinator",handoffs:[reviewer]});
      ticks++;
      console.log(JSON.stringify({event:"staging_tick",tick:ticks,elapsed_ms:Date.now()-started,model_called:false,production_execution:false}));
      if (ticks === 3) controller.abort();
    },
  });
  if (ticks !== 3) throw Error("staging_ticks_incomplete");
  console.log(JSON.stringify({event:"staging_complete",ticks,production_execution:false}));
} finally {
  clearTimeout(deadline);
}
