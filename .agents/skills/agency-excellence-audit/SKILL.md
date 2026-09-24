---
name: agency-excellence-audit
description: Audit Vinterro One / Ercan OS agents against the global Agency Excellence Standard. Use when the user asks to improve all agents, make agents world-class/best-in-class, audit agent quality, review agent weaknesses, benchmark specialists, or upgrade the agent organization.
---

# Agency Excellence Audit

Load:
- `AGENTS.md`
- `docs/standards/AGENCY_EXCELLENCE_STANDARD.md`
- `docs/standards/STABLE_AGENT_CORE.md`
- `docs/standards/AGENT_EXCELLENCE_MANIFEST.json`
- `docs/evals/AGENT_EXCELLENCE_AUDIT_2026-09-24.md`
- `docs/evals/AGENT_CHAMPIONSHIP_SUITE_V2.md`
- `docs/standards/WORLD_CLASS_AGENT_RESEARCH.md`

## Procedure

1. Enumerate stable identities in canonical order: Stable Core 1–21, then GitHub Specialist v3 22–52.
2. Inspect routing, source authority, domain skill, QA ownership, regression/certification and current upstream freshness.
3. Classify gaps as: `SOURCE`, `ROUTING`, `TOOL`, `CRAFT`, `EVAL`, `SECURITY`, `ACCESSIBILITY`, `PERFORMANCE`, `DELIVERY`, `BUSINESS`, `LEARNING`.
4. Prefer system/harness remediation over merely lengthening prompts.
5. Update durable standards/evals/manifests and regression tests.
6. Keep stable identity count unchanged unless the role contract, permissions and evaluation criteria are genuinely distinct.
7. Run structural validator/CI.
8. Never mark behavioral or comparative benchmark states passed unless those runs actually executed with evidence.

## Audit output

For each identity record:
`# | agent | tier/domain | strength | gap found | remediation | championship gate | evidence state`.

The audit is incomplete if any stable identity lacks a profile or if a new stable identity can be added without CI detecting missing excellence coverage.
