---
name: upstream-intelligence-scan
description: Broadly research current GitHub/open-source candidates for web, app, UI/UX, design, image/video, social, SEO, automation, testing and agent workflows; then dedupe, qualify and promote only useful upstreams into Ercan OS. Use when the user asks to search GitHub broadly, find every useful repo/tool, improve Ercan OS from open source, or when a qualified-agent task has a material capability/tooling gap.
---

# Upstream Intelligence Scan

Follow root `AGENTS.md`, `UPSTREAM_INTELLIGENCE.md`, `UPSTREAM_TOOLCHAIN.md`, `DISCOVERY_ADOPTION_LEDGER.md`, project adapters and `upstream-adoption-audit` for material integrations.

## Mission

Maximize discovery recall while minimizing production dependency risk.

Interpret “find/add everything useful” as:
- scan broadly across official repos, GitHub search, current web evidence and curated indexes;
- record durable useful knowledge in `docs/upstream/UPSTREAM_INTELLIGENCE_CATALOG.md`;
- deduplicate forks, mirrors and overlapping capabilities;
- classify candidates as `ADOPT`, `ADOPT_WHEN_NEEDED`, `ADOPT_PATTERN_ONLY`, `WATCHLIST`, `SUPERSEDED` or `REJECT`;
- only install/execute/integrate code when a concrete project/task requires it and the audit passes.

## Required scan domains

When the request is intentionally broad, cover as many of these as materially useful:
1. core frontend/meta-frameworks
2. CSS/Tailwind/component libraries/headless UI
3. design systems/tokens/Figma/Storybook
4. motion/3D/creative web
5. screenshot/design-to-code/visual regression
6. browser automation/testing
7. accessibility/performance/web quality
8. SEO/metadata/crawlers/schema
9. image processing/generation/restoration
10. video/motion graphics/social export
11. canvas/editor/page-builder tools
12. icons/assets
13. social schedulers/publishers/analytics
14. Flutter/React Native/mobile
15. WordPress/Gutenberg/WP CLI
16. Shopify/themes/apps/Hydrogen
17. backend/CMS/auth/commerce
18. analytics/telemetry/observability
19. email/newsletter/deliverability test tools
20. maps/geospatial/local guide
21. charts/data visualization
22. agent/MCP/browser/RAG tooling
23. security/supply-chain/CI
24. curated awesome/machine-readable discovery sources

## Search strategy

Start with the local catalog and ledger. Then, if coverage is incomplete:
- search canonical GitHub organizations and topics;
- search for actively maintained projects and current platform successors;
- use curated lists only as candidate indexes;
- prefer official repos and current primary documentation;
- search multiple formulations for ambiguous capabilities;
- use recency/current upstream checks for maintenance/deprecation.

For very large scans, do not attempt to deeply audit every candidate equally. Use a funnel:

`high-recall discovery → dedupe → obvious reject/superseded filter → relevance filter → shortlist → deep audit only for promotion`.

## Candidate record

For durable candidates record at least:
- `owner/repo`
- capability/category
- decision state
- one-line use case/value
- material caution if applicable (archive/deprecation/license/credentials/experimental status)

Do not hardcode fast-changing versions/stars into durable policy unless needed as dated evidence.

## Dedupe rules

Reject or collapse:
- forks/mirrors of an already-canonical upstream with no material independent value;
- multiple UI kits that solve the same task when project identity only needs one primitive layer;
- deprecated projects with maintained successors;
- agent frameworks that add orchestration complexity without a task-specific capability gain;
- tools already fully covered by an adopted canonical capability.

## Promotion rule

Promotion from discovery to active integration requires:
- concrete Ercan OS/project capability gap;
- current upstream status checked;
- provenance/maintenance/license/security reviewed;
- permission/credential/network surface understood;
- operational burden acceptable;
- integration is the smallest useful unit;
- rollback/reversibility considered;
- required QA/eval added.

## Special handling by domain

### UI/design
Prefer primitives/patterns over importing several branded component systems. Brand tokens/project art direction remain authoritative.

### Screenshot/design-to-code
Use the existing `screenshot-production-ui` + `visual-qa-evidence` pipeline. External repos are pattern/benchmark inputs unless a concrete implementation need justifies more.

### Social publishing
Official Meta/X/etc. APIs remain authority. Scheduler repos are architecture references unless explicitly self-hosted after token/security/ops review.

### WordPress/Shopify
Official platform repos and current developer tooling outrank community boilerplates. Archived/deprecated platform tools are superseded.

### Image/video generation
Generative repos/providers are production engines, not final art directors. Deterministic copy/logo/layout/export QA remains mandatory.

### Agent/MCP/browser tools
Use least privilege. Do not expose cookies, broad tokens or authenticated sessions to community tools merely for convenience.

## Output to Orchestrator

Return a compact structured result:
- scan scope/categories covered;
- canonical candidates already adopted;
- new candidates promoted to catalog;
- pattern-only/watchlist items;
- rejected/superseded duplicates worth noting;
- concrete files/standards/skills changed;
- unresolved gaps requiring future task-specific deep audit.

Do not overwhelm final user output with hundreds of repo names unless requested; the durable catalog is the complete artifact.

## Regression expectations

- “GitHub’daki işimize yarayan her şeyi tara” → broad multi-domain scan + durable catalog update, not one search query.
- “tüm ajanları çalıştır ve siteyi hızlandır” → consult upstream intelligence only for performance/tool gaps; do not fan out through unrelated design/social candidates.
- archived canonical candidate with maintained successor → classify `SUPERSEDED`, do not install.
- canonical repo plus multiple forks → keep canonical, reject duplicate forks unless a material independent feature is required.
- awesome list entry → candidate only, never automatically `ADOPT`.
- no concrete project need → catalog/pattern knowledge may be added, but production dependencies stay unchanged.
