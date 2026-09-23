# Upstream Scan — JEV Runtime Extensions

Date: 2026-09-24

## Scope

Reviewed the newly supplied JEV list with emphasis on items 1–10. Items 11–20 were already reviewed and integrated under the Ercan OS Judgment Engine, so this pass avoids duplicate adoption.

## 1. browser-use/jev-ultrafast
Observed: structured DOM/ARIA-oriented browser snapshot; dynamic bounded operations/targets; one judgment request per cycle; target freshness/geometry/occlusion checks; narrow text-generation helper; independent completion verification.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED beneath authorized browser operation.
README benchmark numbers are task-specific evidence, not general guarantees.

## 2. tamaratran/fast-jev-compaction
Observed: Claude Code/plugin + npm library that scores historical tool calls/results, preserves user/assistant text verbatim, pins recent content, drops/truncates re-runnable tool evidence, and falls back when compaction is unsafe/unhelpful.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED for transcript/history compaction.

## 3. vercel-labs/json-render
Observed: schema/catalog-constrained generative UI framework supporting multiple renderers and allowlisted components/actions.
License: Apache-2.0.
Decision: ADOPT_WHEN_NEEDED through Web Builder / Design Quality, not as a Jev core dependency.

## 4. itsmostafa/typesafe-mcp
Observed: static-binary MCP adapter exposing typed Jev judgments to Claude/Codex/pi and custom endpoints.
License: MIT.
Decision: ADOPT_WHEN_NEEDED as the minimal generic MCP option.

## 5. jkudish/jev-mcp
Observed: MCP server with purpose-built verify/screen/find/rerank/classify/decide/compare/extract/review/gate tools, typed validation, confidence thresholds and failure branches.
License: MIT.
Decision: ADOPT_WHEN_NEEDED when specialized semantic tools are required. Security/completion tools remain advisory.

## 6. sharziki/semdecide
Observed: dependency-light CLI/CI semantic predicates/choice/score/filter plus explicit uncertainty/provider-failure exit codes and an opinionated guard recipe.
License: MIT.
Decision: ADOPT_WHEN_NEEDED. Not authorization/sandbox/security proof.

## 7. 0xNatoshi/jev-codex-router
Observed: per-call model + thinking-effort routing, compact judgment state separate from canonical executor replay, fallback/kill-switch/decision-log patterns, and explicit warnings that historical savings are not current guarantees.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / WATCHLIST because exact model ladder, quota economics and Codex internals are volatile.

## 8. GhalebDweikat/winnow
Observed: large Read/Bash/Grep result sieve, block-level relevance judgment, keep-on-error/keep-on-uncertainty rules, reversible cache + recall, optional summaries, and memory-file relevance injection.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED for tool-result ingress filtering. Data egress/privacy review is mandatory.

## 9. devagrawal09/jev-review
Observed: staged structured code review with risk matrix, file/evidence selection, mechanism classification, severity and conditional reviewer routing. README explicitly says findings are review prompts, not defect proof.
License: MIT.
Decision: ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED beneath independent code QA.

## 10. ellipsis-dev/blink
Observed: file-tree search using multiple semantic walkers distributed by Jev probability over file/folder names; traces and result distributions are saved.
Root LICENSE: not observed.
Decision: ADOPT_PATTERN_ONLY. Validate results by reading/searching source; copy no implementation without license confirmation.

## Existing items 11–20
The following were already integrated on 2026-09-24 under Judgment Engine: agent-desktop, typesafe-mario, jev-drone, OneVOneJev, jev-trader, prism-liquidity-agent, neo4jev, jev-curate, Canny and killmyidea.

## Architecture decision

Create one JIT `jev-runtime-extensions` pack beneath `judgment-engine`. Do not create ten new agents. Route `json-render` to existing frontend/web/design owners. Keep all provider credentials optional and external to source control.
