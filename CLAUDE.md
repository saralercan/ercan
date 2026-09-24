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
- 89 = current Vinterro One production runtime agents.
- Never report 52 as the total live Vinterro One agent count.

## Routing contract

All 89 runtime agents are available by manifest role. They are STANDBY by default.

When the user says “tüm ajanları çalıştır”, “bütün ajanları çalıştır”, “ajanları çalıştır”, “run agents” or equivalent:
- do not spawn all 89;
- select the smallest sufficient ACTIVE expert pod;
- keep unrelated agents STANDBY;
- activate a standby specialist later only when new evidence, dependency, risk or domain need appears;
- add independent QA/review at the appropriate stage;
- never claim a subagent ran unless Claude actually delegated via the Agent tool.

Finance routes to `Finance Expert Agent`. Cross-platform commerce routes to `E-commerce Expert Agent` plus only the platform/CRO/analytics/SEO/finance specialists materially required.

Preserve Ercan OS safety, scope, current-source, policy/Human Approval and verification gates. Provider-specific Claude behavior never overrides the shared agent contract.
