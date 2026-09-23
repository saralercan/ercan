# Ercan OS — JEV Runtime Extensions

Status: active
Date: 2026-09-24

## Purpose

Extend the existing provider-optional Judgment Engine with runtime adapters and patterns for browser control, context management, MCP, CI, model routing, code review and repository navigation.

Execution skill: `.agents/skills/jev-runtime-extensions/SKILL.md`.

This standard does not change stable routing identities: **21 Stable Core + 31 GitHub Specialist v3 Extension = 52**.

## Architecture

Parent decision contract:
`observe -> normalize -> bounded judgment -> deterministic policy/risk gate -> act -> verify`.

Runtime extensions may improve one stage, but they do not become policy authority.

## Extension classes

### Action selection
`browser-use/jev-ultrafast` is a reviewed pattern for fast structured browser decisions. Its key contribution is a dynamic legal action/target space plus freshness/occlusion validation before execution.

### Context management
Use two distinct patterns:
- transcript/history compaction: `fast-jev-compaction`;
- large tool-result ingress filtering with reversible recall: `winnow`.

Do not hide the same evidence through both layers without explicit reason. Errors, user constraints, approvals, project rules and current verification evidence are protected state.

### Tool exposure
- `typesafe-mcp`: minimal generic MCP adapter for typed judgment.
- `jev-mcp`: richer purpose-built semantic tools for verify/screen/find/rerank/classify/decide/compare/extract/review/gate.
Choose one surface by task. MCP adapters remain optional; internal TypeSafe SDK integration is still valid.

### Shell / CI
`semdecide` is a reviewed semantic Unix/CI primitive with explicit uncertainty/provider-failure exit paths. It may gate workflow progression only when deterministic evidence/policy has already established that semantic judgment is appropriate.

### Model routing
`jev-codex-router` contributes model/effort routing architecture, bounded decision state, fallback and calibration patterns. Exact model names, quotas and cost assumptions are runtime facts and cannot be frozen into the standard.

### Code review
`jev-review` contributes staged risk/evidence/severity triage. It supplements compilers, tests, static analysis and independent review.

### Repository navigation
`blink` contributes probabilistic file-tree walking for discovery. Path-name semantics are hints; actual source inspection remains required.

### Generative UI
`vercel-labs/json-render` is routed out of Judgment Engine implementation into Web Builder / Design Quality. It is included in this scan because it appeared in the supplied JEV list, but its architectural value is guardrailed generative UI rather than Jev judgment itself.

## Adoption decisions

| Upstream | Decision | License reviewed |
|---|---|---|
| browser-use/jev-ultrafast | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED | MIT |
| tamaratran/fast-jev-compaction | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED | MIT |
| vercel-labs/json-render | ADOPT_WHEN_NEEDED via web/design | Apache-2.0 |
| itsmostafa/typesafe-mcp | ADOPT_WHEN_NEEDED | MIT |
| jkudish/jev-mcp | ADOPT_WHEN_NEEDED | MIT |
| sharziki/semdecide | ADOPT_WHEN_NEEDED | MIT |
| 0xNatoshi/jev-codex-router | ADOPT_PATTERN_ONLY / WATCHLIST | MIT |
| GhalebDweikat/winnow | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED | MIT |
| devagrawal09/jev-review | ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED | MIT |
| ellipsis-dev/blink | ADOPT_PATTERN_ONLY | root license not observed |

Items 11–20 are inherited from `JUDGMENT_ENGINE.md` and remain deduplicated.

## Completion contract

A runtime extension is VERIFIED only when:
- its exact task boundary is explicit;
- provider/tool actually ran when claimed;
- privacy/credential boundary is satisfied;
- uncertainty/failure/fallback behavior is tested;
- context pruning is reversible or safely reproducible as designed;
- output is independently validated against source/runtime evidence;
- no extension bypasses deterministic permissions/policy/completion gates.
