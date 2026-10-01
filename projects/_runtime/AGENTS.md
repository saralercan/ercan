# Vinterro One — Runtime Project Adapter

This adapter is the mandatory fallback for any active Vinterro One project that does not yet have a dedicated `projects/<slug>/AGENTS.md`.

## Load order
1. repository root `AGENTS.md`
2. `docs/standards/VINTERRO_PROJECT_REGISTRY.json`
3. `docs/standards/VINTERRO_RUNTIME_AGENT_MANIFEST.json`
4. `docs/standards/AGENCY_EXCELLENCE_STANDARD.md`
5. `docs/standards/QUALIFIED_AGENT_ROUTING.md`
6. `docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md`
7. task-relevant domain/platform standards and skills
8. current project/source/provider evidence

## Project resolution
- If an authorized live Vinterro One registry is available, resolve the project from `public.ercan_os_projects` and current project-scoped agents from `public.ercan_os_agents`.
- Treat the live active registry as authoritative for project existence, lead identity, status, version and project-scoped specialist availability.
- If live access is unavailable, resolve from `docs/standards/VINTERRO_PROJECT_REGISTRY.json`.
- A project is never excluded from Vinterro One merely because it lacks a dedicated filesystem adapter.
- Dedicated adapters are project-specific enrichment, not the definition of project existence.

## Routing
For an identifiable project:
- activate its current project lead first;
- add every active project-scoped specialist with a distinct material contribution;
- add every qualified global specialist needed for platform, design, content, data, security, performance, SEO, mail, browser/runtime, deployment or other task requirements;
- add an independent reviewer/QA lane whenever verification is material;
- add Supervisor / Arbiter / Meta Audit / Release Gate according to the supervision and risk contracts.

For `tüm ajanları çalıştır`, `bütün ajanları çalıştır`, `use all agents` and equivalents, build the complete materially relevant ACTIVE pod. Do not literally execute the whole registry and do not minimize the pod when additional non-redundant specialists materially improve the result.

## Platform and source safety
- Never infer a project's implementation platform only from its name or historical context.
- Inspect the current repository/provider/source before mutation.
- Preserve explicit do-not-touch rules across all workstreams.
- External mutation, send, publish, deploy, auth/security, payment, DNS and destructive operations require current evidence and applicable approval/release gates.
- Never claim a specialist, provider action or runtime check ran without evidence.

## Completion
Use only `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT_VERIFIED`, based on current task-relevant evidence.
