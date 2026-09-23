# Upstream Scan — Jev / Judgment Engine

Date: 2026-09-24

## Provider verification

TypeSafe's official SDK and skill describe System One/Jev as a typed-decision layer returning probabilities rather than generated text. Reviewed official JavaScript and Python SDKs expose a System One request model and the official skill instructs developers to keep known rules/calculations/execution in code.

Primary provider references:
- `typesafe-ai/skills`
- `typesafe-ai/typesafe-sdk-js`
- `typesafe-ai/typesafe-sdk-python`
- current official TypeSafe API/docs

Decision: ADOPT_WHEN_NEEDED as a replaceable judgment provider; never a new stable agent.

## Reviewed projects

### lahfir/agent-desktop
Observed: macOS accessibility-tree desktop automation, stable snapshot/element refs, progressive skeleton traversal, structured JSON, session traces, explicit OS permission model.
License: Apache-2.0.
Decision: ADOPT_WHEN_NEEDED for authorized desktop automation.

### fhshaik/typesafe-mario
Observed: emulator RAM/telemetry -> compact canonical JSON -> bounded controller action; timing arithmetic remains code-side.
Root license file: not observed.
Decision: ADOPT_PATTERN_ONLY.

### RomanSlack/jev-drone
Observed: MuJoCo drone simulation with high-rate deterministic flight control and safety reflex, slower Jev tactical judgment.
License: MIT.
Decision: ADOPT_PATTERN_ONLY, simulation/control-architecture research only.
Key lesson: safety/control retains authority; state design must contain the evidence needed for the action.

### emrickgarrett/OneVOneJev
Observed: server-authoritative browser FPS; structured state feeds multiple bounded action judgments; deterministic heuristic fallback.
Root license file: not observed.
Decision: ADOPT_PATTERN_ONLY.

### jarrodwatts/jev-trader
Observed: Monad/Kuru market-making experiment, strict per-block latency budget, dry-run mode, late-decision hold behavior, explicit position/gas accounting.
License: MIT.
Decision: ADOPT_PATTERN_ONLY for latency/backtest/risk architecture; no default live financial execution.

### irfndi/prism-liquidity-agent
Canonical repo resolved from the shortened/social reference.
Observed: liquidity-agent architecture with paper trading default, risk gates, simulation/backtest/replay paths and explicit provider fallbacks.
License: MIT.
Decision: ADOPT_PATTERN_ONLY for risk-gate/paper/replay architecture; no default live financial execution.

### jexp/neo4jev
Observed: graph navigation where outgoing edges are bounded Choice candidates; separate goal-reached judgment; beam-search ranking with budget/caps.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.

### AkashPriyadarshii/jev-curate
Canonical owner spelling resolved during review.
Observed: JSONL/Parquet streaming curation with deterministic host prefilters, parallel typed rubrics, keep/reject thresholds and verbatim outputs.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
README performance/cost claims remain unverified marketing/benchmark claims until reproduced.

### qkal/Canny
Observed: coding-agent supervision layer with append-only evidence ledger. Deterministic facts can enforce completion gates; Jev-based semantic judgments are optional/advisory.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED beneath Ercan OS execution governance.
This aligns strongly with Ercan OS's existing evidence-before-VERIFIED contract.

### monteduro/killmyidea
Observed: multi-dimensional Jev scoring followed by deterministic weighted score, clarity gate and versioned verdict thresholds.
Root license file: not observed.
Decision: ADOPT_PATTERN_ONLY beneath Founder Operations; no objective startup verdict or guaranteed outcome claim.

## Architecture decision

Create one JIT `judgment-engine` capability backed by official TypeSafe sources and selected community patterns. Do not create ten stable agents. Integrate Canny concepts into execution governance; keep desktop automation permission-scoped; treat finance/physical-control repos as bounded research patterns only.

No upstream code is installed or executed by this integration and no provider credential is stored.
