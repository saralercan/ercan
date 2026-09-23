---
name: execution-governance
description: Add disciplined goal framing, baseline inspection, systematic debugging, minimal-change reasoning, verification-before-completion and retirement of invalid fallbacks/duplicate owners to non-trivial Ercan OS implementation work. Use when bugs, regressions, risky edits, cross-module contracts or repeated failed fixes are present.
---

# Execution Governance

This JIT capability adapts useful engineering-discipline patterns from `GanyuanRan/Aegis` while keeping Ercan OS root rules, project adapters, security boundaries and completion authority in control.

## Core principle
`goal -> baseline -> owner -> smallest sufficient change -> proportional verification -> retirement/cleanup -> evidence-backed completion`

## Stable-owner mapping
- Goal/baseline/task contract -> `@Orchestrator`
- Debug/root cause -> task-domain implementation owner + independent QA
- Architecture boundary -> `@WebArchitecture` / platform architect / relevant owner
- Security-sensitive change -> existing security capability + independent QA
- Completion evidence -> `@Orchestrator + @ProductionQA` or task-relevant QA

## Reviewed upstream
- `GanyuanRan/Aegis` — MIT — method pack, not runtime authority.
- Useful patterns: fast path, goal framing, systematic debugging, canonical-owner repair, minimality checks, verification-before-completion, retirement of obsolete fallbacks/duplicate responsibility.
- Aegis itself states that user/project rules outrank it and that it is not final completion authority; Ercan OS preserves that boundary.

## Fast path vs governed path
Use the fast path for trivial, reversible, single-owner work with obvious acceptance criteria.
Use governed path when any of these appear:
- bug/test failure/regression/unexpected behavior
- shared contract or cross-module change
- auth/security/data migration/persistence
- fallback/adapter/compatibility path
- repeated failed fixes
- unclear canonical owner
- architectural change or new responsibility
- production-critical deployment risk

## Debugging contract
1. Reproduce or collect concrete evidence.
2. Locate the canonical owner; do not patch symptoms downstream without owner proof.
3. State change necessity: no-change / docs-config / code-change / blocked.
4. Prefer the smallest sufficient owner-level repair, not the smallest textual diff.
5. Test one causal hypothesis at a time.
6. If repeated fixes fail, stop patch stacking and reassess architecture/ownership.
7. Verify original reproduction plus risk-appropriate regression surface.
8. Retire or explicitly track obsolete fallback/duplicate responsibility introduced or discovered by the change.

## Completion supervision pattern

Reviewed upstream: `qkal/Canny` (MIT).

Adopt its strongest separation as a pattern:
- deterministic facts may enforce completion gates;
- semantic judgments may classify or annotate ambiguous claims/rule conflicts;
- a probabilistic judgment must not silently become an irreversible blocker.

For material coding work, consider a lightweight evidence ledger covering edits, checks and failures. If code changed after the latest passing relevant check, completion remains unverified until an appropriate check passes or the task explicitly documents why no check applies.

When a bounded semantic question materially helps — for example, whether the final message actually claims completion — `judgment-engine` may be loaded. For CLI/CI semantic predicates, Jev review triage or completion-oriented MCP tooling, `jev-runtime-extensions` may also be loaded. SemDecide/jev-review/jev-mcp outputs remain advisory unless a deterministic project rule explicitly and safely consumes them; the Ercan OS evidence gate remains authoritative.

## Anti-overhead rule
Governance must reduce rework, not create ceremony. Do not create branches, specs, ADRs or workspace records solely because this skill loaded. Create durable artifacts only when task risk/complexity or project rules justify them.

## Completion gate
Do not mark VERIFIED until current evidence supports the requested outcome, affected boundaries were checked proportionally, known residual risk is stated and no unverified workaround is presented as a root fix.
