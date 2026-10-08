# Claude Adapter — Vinterro One / Ercan OS

This file is a Claude Code adapter, not a second source of truth.

Before material work:
1. Read `AGENTS.md`.
2. Read `docs/standards/PORTABLE_AGENT_RUNTIME.md` when agent routing is relevant.
3. Read `docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json` JIT when selecting a runtime specialist.
4. Use `.claude/agents/vinterro-router.md` for multi-domain work or any “tüm/bütün/ajanları çalıştır” master trigger.
5. Load only task-relevant domain standards/skills/project context.

## Agent-count contract

- 52 = stable architectural routing identities.
- The live Vinterro One runtime count is read from the live `ercan_os_agents` registry.
- `VINTERRO_RUNTIME_AGENT_MANIFEST.json` and `AGENT_EXPERTISE_SOURCE_MATRIX.json` are versioned mirrors, not a permanent count authority.
- Never report 52 as the total live Vinterro One agent count, and never turn an older snapshot into a hardcoded validator invariant.

## Routing contract

All manifest runtime roles are available by role and are STANDBY by default.

When the user says “tüm ajanları çalıştır”, “bütün ajanları çalıştır”, “ajanları çalıştır”, “run agents” or equivalent:
- activate the complete non-redundant ACTIVE pod of every materially contributing specialist for the current task;
- include the project lead and independent QA/reviewer roles;
- do not optimize for minimum headcount;
- keep unrelated or redundant agents STANDBY;
- do not perform literal full-registry fan-out;
- apply the same contract across ChatGPT/OpenAI, Codex and Vinterro One;
- add independent QA/review at the appropriate stage;
- never claim a subagent ran unless Claude actually delegated via the Agent tool.

Sales intelligence, prospect discovery/enrichment, Vinterro Keşif-to-sales scans, and missing/broken website lead research route through `.claude/agents/sales-intelligence.md` and the canonical Sales Intelligence standard/skills. That agent is research/qualification-only and hands qualified accounts to the outreach/mail execution chain.

Finance routes to `Finance Expert Agent`. Cross-platform commerce routes to `E-commerce Expert Agent` plus only the platform/CRO/analytics/SEO/finance specialists materially required.

Preserve Ercan OS safety, scope, current-source, policy/Human Approval and verification gates. Provider-specific Claude behavior never overrides the shared agent contract.
