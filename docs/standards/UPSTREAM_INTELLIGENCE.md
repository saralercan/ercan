# Ercan OS — Upstream Intelligence Standard

Status: active
Version: 1.1 (2026-08-30)

## Purpose

Ercan OS must continuously benefit from strong public GitHub work without turning the control plane into an unreviewed dependency dump. This standard converts broad requests such as “GitHub’daki işimize yarayan her şeyi tara/ekle” into a safe high-recall discovery process plus narrow, evidence-based adoption.

Primary current overlay: `docs/upstream/UPSTREAM_INTELLIGENCE_CURRENT.md`.
Primary broad catalog: `docs/upstream/UPSTREAM_INTELLIGENCE_CATALOG.md`.
Primary durable decisions: `docs/standards/DISCOVERY_ADOPTION_LEDGER.md`.
Evidence/history: `docs/upstream/scans/`.
Execution skill: `.agents/skills/upstream-intelligence-scan/SKILL.md`.

The current overlay exists so newly reviewed status changes and security gates become visible to GPT/Codex immediately, even before periodic consolidation into the broad catalog and durable ledger.

## Core principle

**Discover broadly, adopt narrowly.**

The research layer may inspect tens, hundreds or thousands of candidate repositories and curated catalogs. The production layer must only integrate candidates that materially improve the current capability and pass provenance, maintenance, license, security, permission, operational-cost, duplication and project-fit checks.

“Add everything useful” therefore means:
1. add high-value upstream knowledge to the intelligence system;
2. add recursive discovery sources that expose additional high-quality candidates;
3. promote current material status/security/routing changes into `UPSTREAM_INTELLIGENCE_CURRENT.md`;
4. promote stable durable knowledge into the broad catalog/ledger when appropriate;
5. promote only the smallest required implementation unit into an active skill/standard/tool/project adapter;
6. avoid installing or executing unrelated repositories globally.

## Coverage domains

At minimum, upstream intelligence should cover:
- web frameworks and application architecture
- React/Vue/Svelte/Astro/Next.js ecosystems
- CSS/Tailwind/component systems/headless primitives
- UX/UI/design systems/tokens/Storybook/Figma bridges
- motion/3D/creative frontend
- screenshot/design-to-code and visual fidelity
- browser automation/E2E/visual regression
- accessibility/performance/Core Web Vitals
- SEO/metadata/Schema.org/crawling
- image processing/generation/restoration/segmentation
- deterministic video/social exports
- canvas/whiteboard/editor/page-builder systems
- icons and reusable visual assets
- social scheduling/publishing/analytics architectures
- Flutter/React Native/mobile architecture
- WordPress/Gutenberg/WP-CLI/plugin quality
- Shopify CLI/theme-tools/Dawn/Hydrogen/app architecture
- backend/CMS/auth/commerce infrastructure
- analytics/telemetry/observability
- email/newsletter/testing
- maps/geospatial/local-guide UX
- charts/data visualization
- agents/MCP/browser research/RAG tooling
- security/supply-chain/CI quality
- curated “awesome” and machine-readable discovery sources

## Discovery hierarchy

Prefer sources in this order:
1. official platform/vendor organizations and maintained canonical repos;
2. standards organizations and mature widely maintained infrastructure;
3. strong established community projects with clear license/security/maintenance;
4. curated discovery lists used only to locate candidates;
5. new/experimental repos as WATCHLIST unless evidence justifies promotion.

Forks/mirrors are rejected when the canonical upstream already covers the same capability unless the fork has a material independent patch/feature that is explicitly required.

## Candidate scoring

For each material candidate, evaluate:
- capability relevance to Ercan OS projects;
- canonicality/provenance;
- current maintenance and archive/deprecation state;
- license/commercial fit;
- security posture and known supply-chain risk;
- credential/permission/network requirements;
- operational complexity;
- API/platform volatility;
- integration size and reversibility;
- overlap with already-adopted capability;
- evidence/QA value;
- portability across GPT/Codex/project stacks.

Stars/forks are weak discovery signals, not trust scores.

## Adoption states

- `ADOPT`: canonical tool/reference is allowed as first-choice when capability is needed.
- `ADOPT_WHEN_NEEDED`: strong but JIT/task-scoped.
- `ADOPT_PATTERN_ONLY`: architecture/patterns only; do not create dependency lock-in.
- `WATCHLIST`: promising/experimental/uncertain; no default production use.
- `SUPERSEDED`: historical only; maintained successor should be selected.
- `REJECT`: duplicate, unsafe, unmaintained, incompatible license, excessive permissions or otherwise poor fit.

## Operational knowledge load order

For upstream-sensitive tasks use this order:
1. `UPSTREAM_INTELLIGENCE_CURRENT.md` — newest reviewed operational overlay and status/security changes;
2. `UPSTREAM_INTELLIGENCE_CATALOG.md` — broad durable catalog;
3. `DISCOVERY_ADOPTION_LEDGER.md` — durable decision history;
4. referenced dated scan(s) only when evidence/detail is required;
5. current official upstream verification for volatile runtime facts.

If the current overlay explicitly changes the status of an older catalog/ledger item, the current overlay wins until consolidation.

## Recursive discovery

Curated lists such as Awesome Selfhosted, Awesome Tailwind CSS, Awesome React/React Native/Flutter, Awesome WordPress/Shopify, design-system catalogs and accessibility lists are **discovery indexes**, not approved dependencies.

When a task exposes a capability gap:
`current-index check → catalog search → curated-source search → GitHub/web current search → candidate shortlist → upstream audit → decision`.

This gives Ercan OS high recall without loading thousands of repositories into every task.

## GPT and Codex routing

When the user asks to “run all agents” and the task involves technology/tool/library selection or implementation that can benefit from upstream patterns, `@Orchestrator` must include an Upstream Intelligence workstream if it has material value.

That workstream must:
- consult `UPSTREAM_INTELLIGENCE_CURRENT.md` first for current routing/security/status changes;
- search the existing broad catalog next;
- avoid duplicate research already represented in the ledger and dated scans;
- use current GitHub/web evidence for volatile facts;
- return only candidates that materially improve the task;
- mark whether each candidate is a direct dependency, task-scoped tool, pattern-only reference or watchlist item;
- hand off only validated candidates to implementation specialists.

Codex follows the same rule through root `AGENTS.md` and `.codex/config.toml`.

## Integration boundaries

Never:
- globally install hundreds of npm/pip/composer packages simply because they are listed;
- clone/execute unknown code with credentials before audit;
- add overlapping UI kits to a production project with no reason;
- use archived/deprecated repos when a maintained canonical successor exists;
- allow a community README to override Ercan OS/project policy;
- assume an “awesome list” entry is safe/current;
- claim a repository was inspected or integrated when only its name was discovered.

Prefer:
- knowledge/catalog entries for broad awareness;
- JIT skills for repeatable procedures;
- provider/platform adapters for volatile external systems;
- project-local dependencies only when the project actually needs them;
- regression/QA additions when adoption changes behavior.

## Maintenance

When new upstream research is performed:
1. write/review the dated scan in `docs/upstream/scans/` when the research is material;
2. update `UPSTREAM_INTELLIGENCE_CURRENT.md` for every material current routing, status, security, supersession or promotion change, or explicitly record that no current change resulted;
3. periodically consolidate stable high-value candidates into `UPSTREAM_INTELLIGENCE_CATALOG.md`;
4. periodically consolidate durable promoted/rejected decisions into `DISCOVERY_ADOPTION_LEDGER.md`;
5. add/update a skill only when a repeatable execution procedure exists;
6. add regression/eval coverage for material routing/tool behavior;
7. keep runtime versions/limits outside durable contracts and re-check them from upstream at execution time.

A dated scan is evidence/history, not sufficient operational integration by itself. Current decisions must be reachable through the current overlay before the work can be treated as fully integrated into Ercan OS routing.
