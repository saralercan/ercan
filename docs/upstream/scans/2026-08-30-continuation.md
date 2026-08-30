# Upstream Intelligence Scan — 2026-08-30 continuation

Status: reviewed discovery record

Scope: current GitHub/open-source changes relevant to Ercan OS web/app/UI/design/video/social/WordPress/Shopify/mobile/security workflows. This is a discovery/adoption record, not permission to globally install or execute community code.

## Promote to durable candidate set

### `flutter/agent-plugins` — ADOPT_WHEN_NEEDED
Official Flutter repository for agent plugins/skills. August 17–21, 2026 work adds a `flutter-app-runtime` Agent Skill for runtime interaction, proactive hot reload, hooks, and synchronized Dart skills. Strong fit for Ercan OS mobile/Flutter work because provenance is canonical and it teaches agents how to interact with a running Flutter application rather than only edit source.

Use: JIT for Flutter app implementation/debugging and agent runtime workflows. Do not load for unrelated web/WordPress/Shopify tasks.

Evidence: https://github.com/flutter/agent-plugins/pulls

### `WordPress/ai` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED
Official WordPress AI plugin/reference. Current work includes connector approvals, AI request logging, permission-gated read abilities, MCP/ability logging APIs, experiments around auditable agent users, and active 1.3.0 development. This is now a stronger source for WordPress-native agent/AI capability boundaries than generic third-party AI plugins.

Use: official architecture/reference for WordPress AI integration; JIT evaluation before enabling production experiments. Project-specific security/capability review remains mandatory.

Evidence:
- https://github.com/WordPress/ai
- https://github.com/WordPress/ai/blob/develop/CHANGELOG.md
- https://github.com/WordPress/ai/issues

### `dotnetdreamer/open-screenshot-generator` — ADOPT_WHEN_NEEDED
Client-side App Store / Google Play screenshot and preview-video production tool. Supports device mockups, multiple store sizes on one canvas, localized layouts including RTL, PNG/MP4 export, and an AI-assisted listing workflow. August 21, 2026 updates added detachable panels and export improvements.

Use: app-store creative/export workflow for Ercan OS mobile products. Valuable because it solves deterministic store-asset production rather than generic social graphics.

Evidence: https://github.com/dotnetdreamer/open-screenshot-generator

### `indranilbanerjee/socialforge` — ADOPT_PATTERN_ONLY
Agency-oriented social production system with brand-aware copy/image/video production, human approval, compliance, failure logging, cost tracking, delivery audits, multi-agent-skill packaging, and Codex compatibility. August 2026 releases expanded validation and delivery-truth checks; current repo reports 20 skills and 260 tests.

Use: borrow production patterns for Ercan OS social workflows: explicit approval gates, delivery audit, no-silent-failure semantics, asset indexes, cost lower-bound reporting, and channel packaging. Do not replace Ercan OS brand standards or official platform APIs.

Evidence: https://github.com/indranilbanerjee/socialforge

### `heldernoid/openstitch` — WATCHLIST / ADOPT_PATTERN_ONLY
Local-first UI design/prototyping system: text/screenshot/sketch → interactive HTML screens on an infinite canvas, shared DESIGN.md, screen linking, play mode, and export. Uses local Ollama by default and includes 50+ design-system references. MIT licensed, but currently very young and explicitly lacks authentication; upstream warns not to expose its ports publicly.

Use: pattern/reference for local design canvas, shared design-system context and prototype flow generation. Do not deploy as a public service without substantial security hardening.

Evidence: https://github.com/heldernoid/openstitch

### `opengeos/GeoLibre` — WATCHLIST / ADOPT_WHEN_NEEDED
Fast-growing local/private GIS platform announced at 5,000+ stars in roughly two months. Runs across browser, desktop, Android and Jupyter and handles GeoJSON, GeoParquet, GeoPackage, Shapefile, COG, LiDAR and 3D Tiles locally.

Use: candidate for analyst/editorial geospatial workflows and heavy local spatial-data inspection. It does not supersede MapLibre/Leaflet for ordinary public guide maps.

Evidence: https://github.com/opengeos/GeoLibre

## Social scheduler dedupe

### `AstaBlackClove/posthive` — WATCHLIST
Self-hostable scheduler with 14+ platform publishing, MCP access, OAuth 2.0 + PKCE, bulk CSV scheduling, templates and per-platform overrides. Distinctive value is MCP-first scheduling without pasting API keys into the agent.

Do not adopt globally yet: Ercan OS already has Postiz-class provider-adapter architecture. Evaluate only if its OAuth/MCP approach materially reduces credential handling or supports a required platform better.

Evidence: https://github.com/AstaBlackClove/posthive

### `jatinder14/hookpost` — REJECT_DUPLICATE / WATCHLIST
Broad scheduler/copilot claiming 30+ networks plus MCP/CLI support. Overlaps heavily with already tracked social schedulers. Keep as discovery-only unless a concrete unsupported platform or API adapter justifies revisiting it.

Evidence: https://github.com/jatinder14/hookpost

## Agentic video

### `Open-Montage/OpenMontage` and mirrors/forks — WATCHLIST / ADOPT_PATTERN_ONLY
Agentic video production architecture combining research, scripting, asset generation, provider selection, Remotion/HyperFrames/FFmpeg composition, resumable state, self-review and pre/post-render validation. Strong architectural overlap with Ercan OS creative pipelines.

Caution: broad GitHub search currently exposes multiple near-identical OpenMontage repos/forks under different owners. Treat provenance/canonicality as unresolved before any dependency adoption. Reuse patterns only until canonical source and maintenance ownership are verified.

Useful patterns: pipeline manifests, renderer selection by visual grammar, pre-compose validation, post-render ffprobe/frame/audio checks, decision logs and cost snapshots.

Evidence: https://github.com/Open-Montage/OpenMontage

## Security status change — HIGH PRIORITY

### August 2026 npm / Keyv / Cacheable Shai-Hulud campaign — ACTIVE SECURITY SIGNAL
External security sources report a large active npm supply-chain campaign beginning with Keyv/Cacheable packages and propagating to hundreds of packages / many malicious versions. Ercan OS Node/JS projects should treat recent npm dependency installs as higher risk until package/lockfile provenance is checked.

Canonical response principle:
- do not trust a clean result from one incident scanner as proof of safety;
- inventory lockfiles and installed dependency versions;
- compare against current primary IOC lists;
- rotate exposed developer/package/cloud credentials when a compromised version executed;
- use npm/package-manager lifecycle-script hardening where compatible;
- prefer official/primary incident sources over copied package lists.

`checker-shai-hulud-2026-08` is ADOPT_WHEN_NEEDED as an offline, read-only incident-specific scanner because it explicitly avoids executing scanned packages and covers npm/pnpm/Yarn/Bun lock/cache/install locations. It is not antivirus and must not become a permanent general security authority.

Evidence:
- https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack
- https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-009/
- https://research.jfrog.com/post/shai-hulud-is-back-august/
- https://github.com/synapse-code-io/checker-shai-hulud-2026-08

## WordPress / Shopify status notes

### WordPress 7.1 responsive block styles — STATUS CHANGE
WordPress developer communication for August 2026 indicates WordPress 7.1 adds responsive block styles with configurable breakpoints through Global Styles/theme.json. Ercan OS WordPress implementations should prefer these native responsive controls where supported instead of adding parallel custom responsive systems without need.

Evidence: https://github.com/WordPress/marketing/issues/1480

### Shopify `theme-tools` — ACTIVE CANONICAL
Theme Tools remains actively maintained in August 2026, including Theme Check changes, Liquid typing/doc work, editor performance and release activity. Existing ADOPT decision remains valid; no replacement needed.

Evidence: https://github.com/Shopify/theme-tools/pulls

## Security rejection note

### SiteGround AI Agent for WordPress <= 1.2.7 advisory — DO NOT ADOPT AS TRUSTED DEFAULT
GitHub Advisory Database published an August 20, 2026 authorization-bypass advisory affecting the SiteGround AI Agent WordPress plugin through 1.2.7. Do not use it as a default WordPress agent integration reference while affected deployments remain in scope; verify patched versions before any project-specific consideration.

Evidence: https://github.com/advisories/ghsa-qg2p-54pj-chvp

## Routing implications

- Flutter/mobile task → consider `flutter/agent-plugins` before community Flutter agent packs.
- WordPress AI/agent task → consult `WordPress/ai` as primary WordPress-native reference before third-party agent plugins.
- App Store / Play Store creative task → consider `open-screenshot-generator` for deterministic screenshots/video exports.
- Social agency production task → reuse SocialForge audit/approval/failure patterns; platform publishing remains official-API-first.
- Local UI prototype/design exploration → OpenStitch may be evaluated in isolated local environments only.
- Geospatial analysis/editorial tooling → GeoLibre may be evaluated; MapLibre/Leaflet remain preferred public-map renderers unless requirements differ.
- Node/npm project work in the current incident window → add supply-chain/IOC verification to security QA.

## Final decisions

- ADOPT_WHEN_NEEDED: `flutter/agent-plugins`, `dotnetdreamer/open-screenshot-generator`, incident-specific Shai-Hulud read-only scanning when relevant.
- ADOPT_PATTERN_ONLY: `WordPress/ai` architecture, `indranilbanerjee/socialforge`, OpenMontage validation/orchestration patterns.
- WATCHLIST: `heldernoid/openstitch`, `opengeos/GeoLibre`, `AstaBlackClove/posthive`.
- REJECT_DUPLICATE unless concrete gap appears: `jatinder14/hookpost` and non-canonical OpenMontage mirrors/forks.
- Security status change: heightened npm supply-chain scrutiny for Node/JS projects during the August 2026 Keyv/Cacheable campaign.
