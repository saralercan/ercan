---
name: judgment-engine
description: Add fast typed semantic judgments to software and agent workflows using a System One-style decision layer. Use when code has a bounded decision/ranking/verification/routing problem that benefits from semantic understanding but does not need generative text. TypeSafe/Jev is the reviewed provider; keep execution, safety and authority in deterministic code.
---

# Judgment Engine

This is a JIT capability, not a new stable agent identity.

Use it when the application already knows the candidate actions or outcomes and needs a fast semantic judgment over current state. The model supplies probabilities/typed answers; **code owns policy, thresholds, side effects, permissions and safety**.

## Canonical provider

Reviewed official upstreams:
- `typesafe-ai/skills` — official Agent Skill, MIT.
- `typesafe-ai/typesafe-sdk-js` — official JavaScript/TypeScript SDK, MIT.
- `typesafe-ai/typesafe-sdk-python` — official Python SDK, reviewed as MIT-licensed repository.
- current TypeSafe docs/API are runtime authority for models, limits, pricing, schemas and provider behavior.

Credential boundary:
- provider access requires `TYPESAFE_API_KEY`;
- never commit, echo, log or persist the key into project artifacts;
- provider availability is optional; do not claim Jev executed unless a real call actually ran.

## Programming model

Map the semantic question to the smallest suitable primitive:
- `Choice` — pick one member of a defined candidate set.
- `Noul` — probability that a condition is true.
- `Score` — position along explicitly described ordered levels.

Prefer one request containing independent questions over the same state when that reduces round trips without creating answer dependencies.

## Stable-owner mapping

- decision decomposition / thresholds / policy -> `@Orchestrator` + task-domain owner
- TypeSafe provider integration -> implementation owner
- codebase completion judgment -> `execution-governance` + independent QA
- desktop action selection -> authorized computer/desktop operator + `@Orchestrator`
- graph traversal -> data/graph owner + `@Orchestrator`
- dataset curation -> data pipeline owner + factual/eval QA
- game/simulation control -> simulation owner
- founder/product scoring -> `founder-operations`; advisory only
- high-risk domains -> deterministic policy/safety owner remains authoritative

## Core design rules

1. **Known facts stay in code.** Exact calculations, hard invariants, permissions, safety constraints and deterministic checks must not be delegated to a judgment model.
2. **Judgments stay bounded.** Give a finite action set or explicit rubric whenever possible.
3. **State must contain the answer.** Missing evidence is a state-design failure; do not blame the model for facts it never received.
4. **Typed output is not truth.** Calibrated probability is evidence, not permission to act.
5. **Separate observation, judgment and action.**
   `observe -> normalize state -> judge -> deterministic policy/risk gate -> act -> verify`
6. **Freshness matters.** A decision made on stale state must not be applied blindly after the world changed.
7. **Use thresholds measured on representative data**, not copied from demos.
8. **Keep a deterministic fallback** when a missing provider must not stall a safe workflow.
9. **Log enough to replay the decision**: normalized state hash/ID, questions, answers/probabilities, selected action, policy gate outcome, latency and downstream result where privacy allows.
10. **Do not ask Jev to generate prose/code/explanations.** Use a generative model only where generative work is actually needed.

## Reviewed application patterns

### Desktop automation — `lahfir/agent-desktop`
ADOPT_WHEN_NEEDED as a desktop-control engine/pattern after local permission and platform review.
Useful pattern:
`accessibility snapshot -> progressive drill-down -> bounded operation choice -> action -> re-observe`.

Current reviewed implementation is macOS-first and requires OS Accessibility permission; screenshots/other surfaces may require additional permissions. Stable refs and accessibility-tree traversal are preferred over pixel guessing when available.

Hard boundary:
- desktop control must stay user-authorized and least-privilege;
- do not silently request broad OS permissions;
- destructive/account/financial/security-sensitive actions retain explicit policy/approval gates.

### Emulator/game loop — `fhshaik/typesafe-mario`
ADOPT_PATTERN_ONLY.
Useful pattern: convert simulator/RAM telemetry to compact canonical state; keep timing arithmetic in code; let the judgment layer choose only legal actions.
No root license file was observed in review, so do not copy implementation code without separate permission/license confirmation.

### Drone simulation — `RomanSlack/jev-drone`
ADOPT_PATTERN_ONLY for simulation and control-architecture research.
Useful pattern:
`high-rate deterministic controller + faster safety reflex + slower semantic tactical judgment`.
The safety controller must retain override authority.
Do not use this capability to create unattended real-world flight control. Physical actuation requires an independently engineered safety/control system and explicit project authorization.

### Browser FPS — `emrickgarrett/OneVOneJev`
ADOPT_PATTERN_ONLY.
Useful pattern: decompose one action tick into independent bounded judgments (move/yaw/pitch/ADS/fire/jump) with deterministic fallback.
No root license file was observed in review; use architecture ideas only.

### Market-making / liquidity demos — `jarrodwatts/jev-trader`, `irfndi/prism-liquidity-agent`
ADOPT_PATTERN_ONLY for simulation/backtest and risk-gate architecture.
Useful patterns:
- isolate semantic market-state judgment from execution;
- hard latency budget and stale-decision handling;
- paper/dry-run mode;
- deterministic position/risk caps that can override model output;
- replay/backtest evidence.

Hard boundary:
- Ercan OS must not turn a probabilistic judgment into autonomous live trading authority by default;
- production financial execution needs explicit user authorization, deterministic risk controls, provider/exchange validation and domain-specific review;
- no performance/profit claim is inferred from demo results.

### Graph navigation — `jexp/neo4jev`
ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Useful pattern: present outgoing graph edges as bounded Choice options; use a separate goal-reached judgment; rank paths using accumulated probabilities; cap breadth/depth/API budget.
Graph traversal remains incomplete when candidate edges were omitted by the retrieval cap; never claim global optimality without coverage evidence.

### Dataset curation — `AkashPriyadarshii/jev-curate`
ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.
Useful pattern:
`cheap deterministic prefilters -> parallel semantic rubrics -> explicit keep/reject thresholds -> verbatim output -> audit stream`.
Benchmark/throughput/cost claims from README are not adopted as Ercan OS facts; measure on the actual dataset/provider plan.

### Completion supervision — `qkal/Canny`
ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED beneath `execution-governance`.
Best pattern: **facts may block; semantic judgments may advise**.
Deterministic ledger facts such as "file changed but no check passed" can enforce a completion gate. A judgment model may classify a completion claim or possible rule violation, but uncertainty must not become an opaque irreversible blocker.

### Startup/product scoring — `monteduro/killmyidea`
ADOPT_PATTERN_ONLY beneath `founder-operations`.
Useful pattern: score several explicit dimensions once, then combine them in deterministic code with versioned weights/thresholds and expose raw diagnostics.
Do not let KILL/FIX/SHIP labels replace founder judgment, market evidence or customer validation.
No root license file was observed in review; copy no implementation code without separate permission/license confirmation.

## When not to use

Do not load the Judgment Engine when:
- a deterministic rule fully solves the decision;
- the task needs open-ended generation rather than bounded judgment;
- required state cannot be safely shared with the provider;
- latency/network dependency would violate the product's safety/reliability envelope;
- the decision is safety-critical and no deterministic independent safety layer exists;
- the only justification is novelty or low model price.

## Verification

Before marking a judgment workflow VERIFIED:
- current official provider docs/schema checked when provider integration changed;
- representative labeled/evaluable cases exercised;
- uncertainty and no-match behavior tested;
- stale-state and provider-failure paths tested;
- side effects gated by deterministic policy;
- secrets stay server-side;
- logs do not leak sensitive state;
- fallback behavior is explicit;
- actual latency/cost/error rate measured when material;
- high-risk domain boundaries preserved.
