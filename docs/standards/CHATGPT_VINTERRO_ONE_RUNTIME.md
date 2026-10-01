# Vinterro One — ChatGPT / GPT Runtime

Status: active  
Version: 1.0  
Date: 2026-10-01

## Purpose

Make ChatGPT/GPT use the same Vinterro One project, specialist, expertise, supervision and release-gate contract as Codex and the native runtime.

The execution semantics are provider-neutral:

`task -> live project resolution -> project lead -> complete materially relevant specialist pod -> evidence/work -> independent QA/reviewer -> correction/retest -> release gate`

## Connection priority

Use the strongest currently available Vinterro One source in this order:

1. **Vinterro One ChatGPT MCP app** — authenticated remote MCP at the Vinterro One Supabase control plane. This is the preferred ChatGPT-native route when the account/workspace supports custom MCP apps.
2. **Connected Supabase app/plugin** — query the live Vinterro One registry directly when ChatGPT custom MCP is unavailable but the authorized Supabase connection is present.
3. **Connected GitHub / repository mirror** — use the versioned portable project/runtime manifests when live Supabase is unavailable.
4. If none of the three is available, do not claim a live Vinterro One connection. Use only already-grounded task context and mark runtime-specific claims `NOT_VERIFIED`.

Live registry state outranks portable mirrors for current project/agent status, version, health and expertise freshness.

## Live sources

Canonical current-state tables:
- `public.ercan_os_projects`
- `public.ercan_os_agents`
- `public.ercan_os_agent_expertise_profiles`
- `public.ercan_os_agent_expertise_health` when available
- Vinterro One supervision tables for independent review/release state

Portable fallback:
- `docs/standards/VINTERRO_PROJECT_REGISTRY.json`
- `docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json`
- `docs/standards/QUALIFIED_AGENT_ROUTING.md`
- `docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md`

## ChatGPT MCP bridge

Edge Function:
`vinterro-one-chatgpt-mcp`

Remote endpoint:
`https://mjigewyqwnkknjbqxjuk.supabase.co/functions/v1/vinterro-one-chatgpt-mcp`

Authentication:
- Supabase Auth OAuth 2.1 / MCP authorization;
- user-scoped token;
- RLS-scoped Supabase client;
- no service-role credential is exposed to ChatGPT;
- MCP function uses its own OAuth middleware, so the Edge gateway JWT check is intentionally disabled for this function only.

Read tools:
- `vinterro_status`
- `vinterro_route_task`
- `vinterro_get_agent`
- `vinterro_get_project`
- `vinterro_get_supervision`

The bridge is intentionally read-first. External writes remain with the actual connected provider/tool and its approval/security gates.

## Required routing behavior

Before substantial Vinterro One project work, resolve the route from current task evidence.

For an identifiable project:
1. resolve the current active project;
2. activate its current project lead first;
3. activate project-scoped specialists with distinct material contribution;
4. add qualified global specialists needed by the task;
5. add independent QA/reviewer for material verification;
6. add security/policy/approval/release roles when risk requires them.

There is **no fixed 5-agent or 8-agent ceiling**. Agent count is a consequence of task scope, not a target.

The master trigger `tüm ajanları çalıştır` and equivalents means the **complete materially relevant pod**, never literal full-registry fan-out and never a minimum-team shortcut.

## ChatGPT execution truth

A returned Vinterro One agent identity is a responsibility contract. ChatGPT may:
- execute that responsibility in the current reasoning/tool session;
- use a real subagent/runtime only when the current surface supports one;
- call provider tools/connectors needed by that specialist.

ChatGPT must not claim multiple persistent agents were independently running unless current runtime evidence proves that execution.

When the live router returns ACTIVE specialists, report them as the selected/active Vinterro One pod. Distinguish selection from actual external execution.

## Expertise freshness

For every selected specialist:
- inspect live expertise state when available;
- if `research_required=true` or expertise state is not `CURRENT`, refresh current authoritative evidence before material domain decisions;
- preserve source hierarchy, provenance and contradiction checks;
- never substitute stale model memory for volatile platform facts.

## Supervision

Material work follows:
`producer -> independent reviewer -> correction/retest -> applicable Release Gate`

A producer cannot self-certify critical work.

Security/auth/RLS/secrets/OAuth/infrastructure/dependency/deploy work additionally requires the Vinterro One security lane and independent security review.

## External actions

Vinterro One routing never grants imaginary provider access.

Send/publish/deploy/database mutation/Shopify mutation/payment/campaign/auth/security/DNS/destructive actions:
- require a real connected provider surface;
- require applicable user/policy approval;
- require direct post-action evidence before success is claimed.

## Completion vocabulary

Use:
- `VERIFIED`
- `PARTIAL`
- `BLOCKED`
- `NOT_VERIFIED`

A correct routing plan alone is not proof that the requested real-world outcome happened.
