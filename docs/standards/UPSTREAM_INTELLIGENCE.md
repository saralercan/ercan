# Ercan OS — Upstream Intelligence Standard

Status: active
Version: 1.0 (2026-08-29)

## Purpose

Ercan OS must continuously benefit from strong public GitHub work without turning the control plane into an unreviewed dependency dump. This standard converts broad requests such as “GitHub’daki işimize yarayan her şeyi tara/ekle” into a safe high-recall discovery process plus narrow, evidence-based adoption.

Primary catalog: `docs/upstream/UPSTREAM_INTELLIGENCE_CATALOG.md`.
Primary decisions: `docs/standards/DISCOVERY_ADOPTION_LEDGER.md`.
Execution skill: `.agents/skills/upstream-intelligence-scan/SKILL.md`.

## Core principle

**Discover broadly, adopt narrowly.**

The research layer may inspect tens, hundreds or thousands of candidate repositories and curated catalogs. The production layer must only integrate candidates that materially improve the current capability and pass provenance, maintenance, license, security, permission, operational-cost, duplication and project-fit checks.

“Add everything useful” therefore means:
1. add high-value upstream knowledge to the intelligence catalog;
2. add recursive discovery sources that expose additional high-quality candidates;
3. promote only the smallest required implementation unit into an active skill/standard/tool/project adapter;
4. avoid installing or executing unrelated repositories globally.

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

## Recursive discovery

Curated lists such as Awesome Selfhosted, Awesome Tailwind CSS, Awesome React/React Native/Flutter, Awesome WordPress/Shopify, design-system catalogs and accessibility lists are **discovery indexes**, not approved dependencies.

When a task exposes a capability gap:
`catalog search → curated-source search → GitHub/web current search → candidate shortlist → upstream audit → decision`.

This gives Ercan OS high recall without loading thousands of repositories into every task.

## GPT and Codex routing

When the user asks to “run all agents” and the task involves technology/tool/library selection or implementation that can benefit from upstream patterns, `@Orchestrator` must include an Upstream Intelligence workstream if it has material value.

That workstream must:
- search the existing catalog first;
- avoid duplicate research already represented in the ledger;
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
1. update `UPSTREAM_INTELLIGENCE_CATALOG.md` for durable high-value candidates;
2. update `DISCOVERY_ADOPTION_LEDGER.md` for material promoted/rejected decisions;
3. add/update a skill only when a repeatable execution procedure exists;
4. add regression/eval coverage for material routing/tool behavior;
5. keep runtime versions/limits outside durable contracts and re-check them from upstream at execution time.
