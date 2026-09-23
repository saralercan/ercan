# Ercan OS — Judgment Engine

Status: active
Date: 2026-09-24

## Purpose

Introduce a provider-optional typed judgment layer for bounded semantic decisions without turning Ercan OS into a Jev-specific architecture.

Execution skill: `.agents/skills/judgment-engine/SKILL.md`.
Runtime extension standard: `docs/standards/JEV_RUNTIME_EXTENSIONS.md` and `.agents/skills/jev-runtime-extensions/SKILL.md` when browser/context/MCP/CI/model-routing/code-review/repo-navigation concerns are material.

Stable routing identities remain unchanged: **21 Stable Core + 31 GitHub Specialist v3 Extension = 52**.

## Architecture

Canonical control flow:

`authoritative observations -> normalized state -> typed judgment(s) -> deterministic policy/risk gate -> side effect -> verification/outcome`

The judgment model does not own:
- permissions
- safety invariants
- exact arithmetic
- hard business rules
- irreversible side effects
- completion authority
- truth claims unsupported by evidence

## Provider priority

For TypeSafe/Jev integrations:
1. current TypeSafe official docs/API;
2. official `typesafe-ai/skills`;
3. official TypeSafe SDK for the project language;
4. reviewed community examples as pattern references.

The provider remains replaceable. Ercan OS code should depend on an internal judgment interface when practical rather than scattering provider-specific calls across business logic.

## Supported semantic primitives

- **Choice** — one option from a bounded set.
- **Noul** — probability of a yes/no condition.
- **Score** — graded ordered assessment.

Use independent questions in a shared request only when they depend on the same input state and not on each other's answers.

## Recommended internal adapter

A project integrating a judgment provider should expose a narrow interface such as:
- `evaluateChoice(state, criteria)`
- `evaluateCondition(state, condition)`
- `evaluateScore(state, levels)`

Provider-specific request/response types stay inside the adapter. Domain policy consumes normalized typed answers and probabilities.

## Confidence and uncertainty

- Never treat probability as permission.
- Set thresholds from task-specific evaluation data and consequence severity.
- Include explicit `no_match`, `unknown` or human-review paths when valid.
- Low confidence can trigger deterministic fallback, defer/retry on fresh state, human review or a reasoning model depending on domain.
- A confidence score is not a global correctness score.

## High-risk boundaries

### Physical systems
Jev-style tactical judgment may be studied in simulation, but real physical control must retain independently validated deterministic safety/control authority. The model must not directly bypass actuator/safety limits.

### Financial systems
Market-state classification and paper/backtest experiments are allowed as research patterns. Live execution is never implicitly authorized by a model prediction; deterministic risk, account permissions and explicit production approval remain separate.

### Security/account changes
A model may help classify risk or intent, but authentication, authorization, secret handling and destructive-operation gates remain deterministic.

## Runtime extensions

The parent Judgment Engine remains the policy boundary. Runtime adapters are selected JIT and must not be globally installed merely because they overlap. Use `typesafe-mcp` for a small generic MCP surface, `jev-mcp` when purpose-built verification/reranking/review tools materially help, `fast-jev-compaction` for history compaction, Winnow-style logic for large tool-result ingress, and SemDecide for CLI/CI predicates. Exact model routing uses current runtime/model availability rather than a frozen ladder.

## Reviewed upstream patterns

- `typesafe-ai/skills` — ADOPT_WHEN_NEEDED / OFFICIAL_REFERENCE / MIT.
- `typesafe-ai/typesafe-sdk-js` — ADOPT_WHEN_NEEDED / OFFICIAL SDK / MIT.
- `typesafe-ai/typesafe-sdk-python` — ADOPT_WHEN_NEEDED / OFFICIAL SDK; re-check current package/repo metadata at use time.
- `lahfir/agent-desktop` — ADOPT_WHEN_NEEDED for authorized desktop automation / Apache-2.0.
- `fhshaik/typesafe-mario` — ADOPT_PATTERN_ONLY / license not established in reviewed root.
- `RomanSlack/jev-drone` — ADOPT_PATTERN_ONLY / MIT / simulation-only for Ercan OS.
- `emrickgarrett/OneVOneJev` — ADOPT_PATTERN_ONLY / license not established in reviewed root.
- `jarrodwatts/jev-trader` — ADOPT_PATTERN_ONLY / MIT / dry-run/backtest architecture only.
- `irfndi/prism-liquidity-agent` — ADOPT_PATTERN_ONLY / MIT / paper/backtest/risk-gate patterns only.
- `jexp/neo4jev` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED / MIT.
- `AkashPriyadarshii/jev-curate` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED / MIT.
- `qkal/Canny` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED / MIT.
- `monteduro/killmyidea` — ADOPT_PATTERN_ONLY / license not established in reviewed root.

## Completion contract

A judgment-engine integration is VERIFIED only if:
- the state/question decomposition is explicit;
- provider access actually exists when claimed;
- representative cases were evaluated;
- uncertainty/failure/stale-state behavior is covered;
- deterministic side-effect gates exist;
- sensitive data/secrets are protected;
- relevant domain QA ran;
- observed results, not README marketing claims, support any performance statement.
