---
name: jev-runtime-extensions
description: Extend Ercan OS Judgment Engine with reviewed Jev/TypeSafe runtime patterns for browser action selection, context pruning/compaction, MCP exposure, Unix/CI semantic decisions, model routing, code review and codebase navigation. Use only when one of these runtime concerns materially benefits from bounded typed judgments; keep deterministic policy, permissions, evidence and fallback authority outside the model.
---

# JEV Runtime Extensions

This is a JIT capability pack beneath `judgment-engine`. It does not create new stable agent identities.

Load `.agents/skills/judgment-engine/SKILL.md` and `docs/standards/JUDGMENT_ENGINE.md` first. The official TypeSafe SDK/docs remain provider authority; community repositories below are runtime adapters and patterns.

## Stable-owner mapping

- browser action selection -> authorized `WebOperator/@BrowserQA` + `@Orchestrator`
- context compaction/pruning -> `@Orchestrator` + execution-governance
- MCP exposure -> tool/MCP integration owner + `@Orchestrator`
- CLI/CI semantic gates -> execution-governance + task-domain QA
- coding-model routing -> `@Orchestrator` + runtime/model-routing owner
- code review -> independent QA/reviewer + execution-governance
- repo navigation -> implementation owner + `@UpstreamIntelligence` when external discovery is involved
- generative UI -> `@FrontendSystem + @BrowserQA + @AccessibilityQA`; delegated to web/design capability packs

## 1. Browser action loop — browser-use/jev-ultrafast

Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED` (MIT).

Useful architecture:
`atomic structured DOM snapshot -> bounded operation Choice -> compatible target Choice -> deterministic executor -> freshness/occlusion check -> re-observe -> independent outcome verification`.

Important properties:
- offer only legal operations/targets observed in the current page;
- keep text generation separate and narrow;
- never execute model output as selectors, JavaScript, shell commands or coordinates;
- re-check target freshness and current geometry before input;
- a model `DONE` decision never proves task completion.

Use only on user-authorized browser surfaces. Playwright/browser evidence and existing approval/auth boundaries remain authoritative. README latency claims are task-specific benchmark evidence, not a general Ercan OS performance guarantee.

## 2. Transcript compaction — tamaratran/fast-jev-compaction

Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED` (MIT).

Best pattern:
- never rewrite user/assistant text merely to save tokens;
- score old tool calls/results for continued usefulness;
- pin recent/critical evidence;
- keep verbatim result when still needed;
- keep call + truncated result when knowing the action matters but full payload is re-fetchable;
- drop only when confidently irrelevant and re-runnable;
- fail/fallback rather than silently corrupt history.

Compaction is not memory deletion and not proof that omitted evidence will never be needed. Preserve project rules, user constraints, errors, approvals, current task state and completion evidence deterministically where material.

## 3. Generative UI — vercel-labs/json-render

Decision: `ADOPT_WHEN_NEEDED` under web/design lanes (Apache-2.0), **not a Jev-specific runtime dependency**.

Useful pattern:
`AI-generated structured spec -> schema/catalog guardrail -> known component/action registry -> deterministic renderer`.

Route implementation through `web-builder-capability-pack` and `design-quality-engine`. Components/actions exposed to generation are an allowlist. Generated UI must not gain arbitrary code execution or permissions. Browser/accessibility/design QA remain required.

## 4. Generic MCP judgment adapter — itsmostafa/typesafe-mcp

Decision: `ADOPT_WHEN_NEEDED` (MIT).

Use when an MCP client needs a small provider-neutral surface for typed `noul/choice/score` judgments.

Rules:
- do not run this and another Jev MCP server merely for redundancy;
- select the narrowest adapter that matches the task;
- keep API keys in MCP server environment/secret storage, never chat or repository;
- custom/local endpoints must be explicitly configured and trusted.

## 5. Purpose-built MCP judgments — jkudish/jev-mcp

Decision: `ADOPT_WHEN_NEEDED` (MIT).

Reviewed tools include claim verification, screening, candidate finding/reranking, classification, bounded decisions, passage comparison, extraction, diff review and completion gating.

Use only as advisory/semantic tooling beneath Ercan OS authority:
- `jev_screen` may estimate injection/relevance but remote content remains untrusted regardless of score;
- `jev_verify` does not replace exact quote/source matching where deterministic checks exist;
- `jev_review/gate` do not replace tests, build results or independent code review;
- malformed/low-confidence responses route to review/fallback rather than automatic acceptance.

## 6. Unix/CI semantic primitive — sharziki/semdecide

Decision: `ADOPT_WHEN_NEEDED` (MIT).

Useful when shell/CI needs stable exit codes for bounded semantic predicates, choices, scores or JSONL filtering.

Use deterministic exit-code handling with a distinct uncertainty/provider-failure path. Semantic `guard` output is not authorization, sandboxing or security proof. Money, credentials, production infrastructure, private data and irreversible operations keep deterministic policy gates.

## 7. Coding-model router — 0xNatoshi/jev-codex-router

Decision: `ADOPT_PATTERN_ONLY / WATCHLIST` (MIT).

Useful architecture:
- compact decision state separate from full executor context;
- select model capability and thinking effort per call;
- explicit fail-open/fallback/kill-switch paths;
- local decision logs for calibration;
- route policy measured on completed tasks/corrections/cost, not target model-share percentages.

Do **not** copy its exact model ladder, quota assumptions or routing thresholds into Ercan OS as permanent truth. Current available models/plans/rates/runtime constraints are volatile and must be resolved at execution time. A routing confidence score is not a success probability.

## 8. Context sieve — GhalebDweikat/winnow

Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED` (MIT).

Useful pattern:
`large tool result -> block segmentation -> relevance/error judgments -> keep uncertain/error blocks -> hide only confident irrelevant blocks -> reversible cache/recall`.

Prefer reversibility over destructive deletion. Never hide error output merely to save context. Data-policy review is mandatory because tool output may be sent to external judgment/summarization providers.

Overlap rule:
- use `fast-jev-compaction` for transcript/history compaction;
- use Winnow-style logic for large tool-result ingress filtering/recall;
- do not stack both blindly if the same evidence could be hidden twice.

## 9. Structured code review — devagrawal09/jev-review

Decision: `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED` (MIT).

Useful staged pattern:
`risk matrix -> file profile -> evidence region selection -> mechanism classification -> severity -> reviewer route`.

Use as a triage/prioritization layer. Findings are hypotheses requiring source/test/static-analysis/runtime evidence. Independent review and deterministic checks remain completion authority.

## 10. Codebase navigation — ellipsis-dev/blink

Decision: `ADOPT_PATTERN_ONLY`.

Useful pattern:
`directory candidates -> semantic probability allocation -> multiple bounded walkers -> candidate file distribution -> traceable result`.

Use for initial repo navigation when filenames/path structure carry useful semantic information. It does not inspect file content while routing and therefore cannot prove where behavior actually lives. Validate returned files by reading/searching the source. No root LICENSE file was observed in review, so copy no implementation code without separate license confirmation.

## Existing JEV application patterns (11–20)

Already covered by the parent Judgment Engine and must not be duplicated as new agents:
- `lahfir/agent-desktop`
- `fhshaik/typesafe-mario`
- `RomanSlack/jev-drone`
- `emrickgarrett/OneVOneJev`
- `jarrodwatts/jev-trader`
- `irfndi/prism-liquidity-agent`
- `jexp/neo4jev`
- `AkashPriyadarshii/jev-curate`
- `qkal/Canny`
- `monteduro/killmyidea`

## Selection rules

Prefer the smallest useful extension:
- browser operation -> Jev Ultrafast pattern
- old transcript pruning -> fast-jev-compaction pattern
- huge tool output before context -> Winnow pattern
- generic MCP typed judgment -> typesafe-mcp
- specialized verification/rerank/review MCP tools -> jev-mcp
- shell/CI predicate -> SemDecide
- model/effort routing -> jev-codex-router pattern
- code-review triage -> jev-review
- filename/tree-first navigation -> Blink
- generative UI -> json-render through web/design lanes

Do not install multiple overlapping adapters globally merely because they exist.

## Security and privacy

- Never persist `TYPESAFE_API_KEY` in source, chat, logs or artifacts.
- Treat provider-bound state as data egress; apply project privacy/data-policy restrictions first.
- Remote content remains untrusted even if a semantic screen scores it as safe.
- No semantic judgment replaces authentication, authorization or irreversible-action approval.
- Local MCP/browser services should bind narrowly and require authentication when exposure exceeds loopback/trusted local use.
- Third-party benchmark/cost/token claims are not promoted as Ercan OS guarantees.

## Verification

Before claiming an extension VERIFIED:
- provider/adapter actually configured when runtime use is claimed;
- representative labeled cases tested;
- malformed/timeout/uncertain response path tested;
- deterministic fallback or escalation exists;
- secrets and sensitive state are protected;
- reversible context pruning can restore evidence when designed to;
- browser/action targets are revalidated before execution;
- code-review/navigation results are confirmed against source/tests;
- generated UI stays inside the approved catalog/action surface;
- independent completion QA still runs.
