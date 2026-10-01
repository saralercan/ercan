# Vinterro One — Runtime Project Manifest

Purpose: portable fallback for every active Vinterro One project without a dedicated adapter.

- Canonical project list: `docs/standards/VINTERRO_PROJECT_REGISTRY.json`
- Live authority when connected: `public.ercan_os_projects`
- Live project-agent authority when connected: `public.ercan_os_agents`
- Shared global specialist pool: Vinterro One runtime registry
- Supervision: producer -> independent reviewer -> correction/retest -> applicable release gate

A missing dedicated adapter is not a blocker. Resolve the active project and lead from the live registry when available, otherwise from the portable project registry, then load task-relevant standards and specialists.

Never hardcode the total project or agent count into routing semantics.
