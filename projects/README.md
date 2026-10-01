# Vinterro One Project Adapters

These folders are the shared Vinterro One project-routing layer. They do not replace the actual application/theme/plugin source repositories.

The **live project registry is authoritative** when connected. This file and `docs/standards/VINTERRO_PROJECT_REGISTRY.json` are portable mirrors so Codex can still route correctly when the live registry is unavailable.

| Project | Runtime slug | Lead | Adapter |
|---|---|---|---|
| Vinterro Digital | `vinterro-digital` | `Vinterro Digital Baş Uzman Ajanı` | `projects/vinterro-digital/` |
| Drag&Drop | `drag-drop` | `Drag&Drop Baş Uzman Ajanı` | `projects/dragdrop/` |
| Ayvalık Vibes | `ayval-k-vibes` | `Ayvalık Vibes Baş Uzman Ajanı` | `projects/ayvalik-vibes/` |
| Go Ayvalık | `go-ayval-k` | `Go Ayvalık Baş Uzman Ajanı` | `projects/goayvalik/` |
| Ayvalık Reklam | `ayval-k-reklam` | `Ayvalık Reklam Baş Uzman Ajanı` | `projects/_runtime/` |
| Vinterro Keşif | `vinterro-kesif` | `Vinterro Keşif Agent` | `projects/_runtime/` |
| Vinterro Studio | `vinterro-studio` | `Vinterro Studio Baş Uzman Ajanı` | `projects/_runtime/` |
| LocalRoot | `localroot` | `LocalRoot Baş Uzman Ajanı` | `projects/_runtime/` |
| Dükkan Ayvalık | `dukkan-ayvalik` | `Dükkan Ayvalık Baş Uzman Ajanı` | `projects/_runtime/` |
| Cotti Cotti | `cotti-cotti` | `Cotti Cotti Baş Uzman Ajanı` | `projects/_runtime/` |
| Vinterro Social OS | `vinterro-social-os` | `Vinterro Social OS Baş Uzman Ajanı` | `projects/_runtime/` |
| FORMÉ | `forme` | `FORMÉ Baş Uzman Ajanı` | `projects/_runtime/` |
| Çiçek Sahaf | `cicek-sahaf` | `Çiçek Sahaf Baş Uzman Ajanı` | `projects/_runtime/` |

## Coverage rule

Every active Vinterro One project is supported by Codex.

- Projects with dedicated adapters use their own `projects/<slug>/AGENTS.md` + `PROJECT.md`.
- Projects without a dedicated adapter use `projects/_runtime/`.
- A missing dedicated adapter **must never** cause a project to fall outside Vinterro One routing.
- When an authorized live registry is available, current active project/agent state from `public.ercan_os_projects` and `public.ercan_os_agents` outranks this mirror.
- New projects added to the live registry are immediately eligible for runtime fallback routing; they do not require a Codex code change before Vinterro One can use them.

## “All agents” semantics

`tüm ajanları çalıştır`, `bütün ajanları çalıştır`, `ajanları çalıştır`, `use all agents` and equivalents mean:

**activate the complete materially relevant ACTIVE pod** = project lead + distinct project-scoped specialists + qualified global specialists + independent QA/reviewer + applicable security/supervision/release gates.

It does not mean literal full-registry fan-out, and it must not be reduced to a single project agent when distinct specialists materially contribute.

## Source-repository rule

When an actual project source repository is connected, add a small repo-local `AGENTS.md` that points back to the central Vinterro One contract and records only project-specific deltas/context. Do not fork the full constitution into every repository.

## Deployment reality

A project adapter is routing policy, not proof of current hosting/Git linkage. Before production writes, inspect the actual provider/account/source state. Existing live systems must be reconciled/backed up before any deployment path that can overwrite production files.
