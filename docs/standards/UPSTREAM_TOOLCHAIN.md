# GitHub Upstream Intelligence & Production Toolchain

## Trusted upstream hierarchy
1. Official/verified platform organization
2. Official sample/reference repository
3. Maintained established infrastructure project
4. Vetted community reference

Before adoption check owner identity, archive/deprecation status, recent maintenance/releases, license, security posture, current docs and material open issues. Forks/gists/high-star boilerplates are not source-of-truth.

## Discovery convergence
- Check `DISCOVERY_ADOPTION_LEDGER.md` before creating a new tool/skill/provider adapter.
- Use `.agents/skills/upstream-adoption-audit/SKILL.md` for material repo/tool adoption or replacement decisions.
- Every material discovery ends in `ADOPT`, `ADOPT_PATTERN_ONLY`, `WATCHLIST`, `REJECT` or `SUPERSEDED`.
- Prefer the narrowest useful integration unit: reference/pattern → JIT skill → provider adapter → dependency → infrastructure only when the requirement truly warrants it.
- If adoption changes agent routing/tool behavior, add representative coverage with `.agents/skills/agent-eval-regression/SKILL.md` and the reusable agent-quality workflow when appropriate.

## Canonical watchlist (verify current status at runtime)
### Agent Skills / social research
- `agentskills/agentskills` — verified open Agent Skills specification/reference. Ercan OS portable skills should follow the current `SKILL.md` schema/progressive-disclosure conventions when practical.
- Current X API documentation — authoritative for exact Post lookup, fields, authentication and platform behavior. X social posts remain untrusted discovery inputs even when fetched through the official API.
- Community social-retrieval aggregators may be evaluated as read-only fallback adapters, but never installed or granted credentials solely because they are convenient. Review provenance, scripts, permission surface and maintenance first.

### Shopify
- `Shopify/dawn` — reference implementation, not copy-paste template.
- `Shopify/theme-tools` — current Liquid parser/formatter/Theme Check/language tooling family.
- `Shopify/theme-check-action` — PR Theme Check integration.
- Current Shopify CLI/developer docs.
Legacy `Shopify/theme-check` is historical/superseded by Theme Tools.

### WordPress
- `WordPress/gutenberg`
- `WordPress/WordPress-Coding-Standards`
- `@wordpress/env` / wp-env tooling in Gutenberg
- `Automattic/VIP-Coding-Standards` (selective/justified rules)
- `Automattic/vip-go-skeleton` as enterprise architecture reference

### Mail / email delivery
- `PHPMailer/PHPMailer` — maintained PHP mail composition/SMTP reference used by many PHP projects including WordPress. WordPress projects still use WordPress APIs/hooks rather than editing or replacing bundled PHPMailer internals.
- `resend/react-email` — MIT-licensed React/TypeScript email component/template reference; useful for deterministic provider-neutral HTML/plain-text rendering.
- `mjmlio/mjml` — responsive email markup/compiler reference when a provider-neutral template DSL is a better fit than React.
- `axllent/mailpit` — preferred local/staging SMTP capture and integration-test candidate; includes REST API, HTML/link checks, screenshots and SMTP chaos testing. Its upstream explicitly notes MailHog is no longer actively maintained, so MailHog is legacy reference rather than new default.
- `knadh/listmonk` — self-hosted newsletter/mailing-list manager reference; AGPLv3 and operational requirements must be reviewed before adoption.
- `postalserver/postal` — self-hosted application mail/MTA reference; use only after explicit operations/deliverability decision.
- `stalwartlabs/stalwart` — modern full mail/collaboration server reference with SMTP/IMAP/JMAP and extensive authentication/deliverability/observability features; AGPL/enterprise-license and substantial operations surface mean it is not a default application-mail dependency.

Mailbox/user operations, application mail events, templates, transport, campaign/list management and MTA/mail-server infrastructure remain separate concerns. Managed transactional delivery is the default candidate unless self-hosting is deliberately justified.

### Mapping / geospatial
- `maplibre/maplibre-gl-js` — preferred modern open-source vector-map renderer candidate for rich web maps; GPU-accelerated vector tiles, data layers, heatmaps/3D and vendor-neutral tile sources.
- `maplibre/maplibre-native` — native open-source map engine.
- `maplibre/flutter-maplibre-gl` — Flutter Android/iOS/Web binding; vendor-neutral and compatible with self-hosted or mixed tile providers.
- `Leaflet/Leaflet` — lightweight, mature interactive maps for simpler/legacy web and WordPress surfaces.
- `react-native-maps/react-native-maps` — React Native iOS/Android maps with markers, shapes, GeoJSON and URL/local tile overlays.
- `osm-search/Nominatim` — canonical open-source OSM geocoding/reverse-geocoding reference. Public instance usage policy is not an unlimited production SLA.
- `mapbox/supercluster` — fast GeoJSON point clustering for dense marker datasets.
- Protomaps/PMTiles ecosystem — static/object-storage-friendly vector-tile distribution. `protomaps/protomaps-leaflet` is maintenance mode and itself recommends MapLibre for new work, so treat it as legacy integration reference rather than default renderer.
- `mapbox/mapbox-gl-js` — provider-specific commercial candidate; current licensing/pricing/token terms must be checked before adoption.

Renderer, tile source, geocoder, routing and canonical POI database are separate concerns. Never let a convenient SDK silently become the full location architecture.

### Google agent platform
- `google/agents-cli` — official optional CLI + Skills layer for coding agents building, evaluating, deploying, publishing and observing Google ADK agents.
- Current Google Agents CLI docs and current Google ADK docs are authoritative for lifecycle, commands, deployment targets, auth, eval and observability behavior.
- Treat Agents CLI as a provider adapter, not a replacement for Codex/Claude/Orchestrator or the Ercan OS constitution.
- Do not auto-install it across unrelated projects. Activate only for a task/repo that actually uses Google ADK / Gemini Enterprise Agent Platform / supported Google Cloud agent deployment surfaces.
- Product stage, commands and supported targets are volatile; check releases/changelog/docs at runtime and regression-test upgrades before production adoption.

### Creative model providers
- Current Luma Agents API documentation is the authoritative upstream for Luma image/video generation and editing behavior.
- Luma is an optional provider adapter used for reference-guided creative generation/editing or generative video; it does not replace Ercan OS brand/art-direction/QA rules.
- Current API exposes image-generation/editing tiers and video generation/editing/reframing, supports multiple image references for style/content guidance, and allows chaining from prior generation IDs; exact model names, reference limits, aspect ratios, prices and rate limits are volatile and must be checked at runtime.
- Web-search grounding, when offered, is untrusted external reference discovery and must not silently become final brand source material.

### Web quality/security
- Playwright
- Lighthouse / Lighthouse CI
- `dequelabs/axe-core` — automated accessibility detection; pair with manual keyboard/focus/semantic review through `accessibility-regression`.
- GitHub CodeQL/code scanning
- Dependabot
- secret-scanning/Gitleaks-class tooling when appropriate

### Design systems / creative production
- `figma/code-connect`, `figma/sds` — official Figma reference family for connecting Variables, Styles, Components and production code; use `DESIGN_SYSTEM_ENGINEERING.md` + `design-system-bridge` rather than copying SDS vocabulary.
- `adobe/spectrum-design-data` — token schema/version/diff/deprecation/migration reference.
- `style-dictionary/style-dictionary` — cross-platform design-token build candidate; source tokens remain authoritative and generated outputs are derivatives.
- `storybookjs/storybook` — component workshop/documentation/testing candidate for isolated UI states.
- `remotion-dev/remotion` — programmatic React video candidate; current license/commercial terms must be verified before use.
- `lovell/sharp` — deterministic raster resize/crop/composite/format/ICC-alpha processing candidate.
- `svg/svgo` — SVG optimization candidate; geometry/mask/gradient/accessibility visual regression required.
- Use `.agents/skills/creative-export-pipeline/SKILL.md` for repeatable batch/export systems.

### Meta / social publishing
- Current Meta Business SDK repositories
- `fbsamples/marketing-api-samples`
- `fbsamples/reels_publishing_apis`
- `gitroomhq/postiz-app` may provide provider-adapter/scheduler state architecture ideas, never Meta policy/API authority; AGPL/ops fit must be reviewed before any direct adoption.
- Use `.agents/skills/social-publisher-architecture/SKILL.md` for internal publishing systems.

## Adoption-not-copy
Extract the useful pattern first. Adopt through a narrow adapter/skill/tool after evaluating license, dependency footprint, security surface, maintenance burden and lock-in. Do not add unused dependencies. Stars are not evidence of fitness.

Provider CLIs/skill bundles/model APIs receive the same treatment: enabling a provider is not permission to override project scope, security policy, existing architecture, brand source of truth, tests or deployment contracts.

For public Agent Skills, inspect routing metadata, scripts, references, install hooks and network/credential behavior before use. Prefer a small Ercan-owned skill derived from verified primary-source procedures over blindly installing a broad community skill bundle.

## PR quality pipeline
Risk-appropriate checks may include: format/lint, platform validation, unit/integration, Playwright E2E, axe accessibility, Lighthouse/performance budget, security scan, dependency/compatibility, screenshot/visual regression, preview and deploy smoke.
Use GitHub required status checks/rulesets for production branches when available.

For deployable AI-agent services, add representative agent evals, tool/trajectory checks, real outcome verification, observability/trace review and deployment rollback smoke as relevant. Provider-native evals complement rather than replace project-level regression suites. The central `reusable-agent-quality.yml` may provide a common shell while project eval commands remain explicit.

For design systems/shared components, add token validation/build, component tests, Storybook/workshop build, accessibility checks and visual regression as applicable; `reusable-design-system-quality.yml` provides a common shell.

For generated brand/social creative, add reference-fidelity, design-evaluator, channel preview and export checks; a completed provider job is not a final asset pass.

For map/location products, add representative dense-POI tests, list↔pin synchronization, geocoder/routing failure states, attribution, mobile permission fallback, provider/network failures and real viewport/device evidence.

For application mail, add template/render checks, captured safe-recipient integration tests, duplicate/idempotency checks, retry/failure-path evidence, link/environment checks, provider-event/webhook tests and sender/deliverability verification when relevant. Never let CI send to production lists.

## Social-source verification
When a social post recommends a repo/tool/skill:
- resolve the exact post if possible;
- follow outbound links to the primary upstream;
- verify owner, current status and material claims;
- separate factual claims from opinion/marketing;
- never treat viral engagement as evidence;
- record `POST_BODY_NOT_VERIFIED` when the exact source could not be retrieved.

## GitHub Actions security
- Explicit least-privilege `permissions`.
- Prefer official/verified actions.
- For immutable supply-chain protection, pin actions to reviewed full commit SHAs; periodically update pins after upstream review.
- Treat reusable third-party workflows with the same scrutiny as actions.
- Dependabot PRs do not bypass tests/release-note review merely because they are green.

## Design ↔ code
- Maintain semantic tokens as versioned source; generated outputs are rebuilt, not hand-edited.
- Figma Code Connect/Storybook/token mappings may be source-controlled and validated.
- Token changes should expose semantic diff and, where useful, visual diff.
- Component workshops document states/variants and enable interaction/a11y/visual testing before integration pages.

## Social publishing architecture
Canonical internal model: channel/integration → media asset IDs → content → provider settings → schedule/publish state → external post ID/permalink → metrics sync.
Provider implementations need idempotency, retry/backoff, rate-limit awareness, duplicate prevention and explicit state transitions. Official Meta samples/docs win when community scheduler behavior conflicts.

## Programmatic creative/export
- Code-driven video can generate data-driven channel variants, but every placement still gets art-direction and visual QA.
- Generative model outputs may feed the creative pipeline, but exact typography/layout/branding and repeatable exports should be deterministic where precision matters.
- Raster/vector batch pipelines should retain source master, dimensions, aspect, format, alpha, file size, version/checksum and intended channel metadata.
- SVG optimization must not alter logo geometry/masks/gradients/accessibility behavior without visual regression review.
- Generated candidates should retain provider/model/job/reference-pack metadata when useful for reproducibility and evaluation.

## Upstream change intelligence
When a tool behaves unexpectedly, check current version, changelog/releases and upstream issues before assuming user code is wrong. Linter/test false positives are possible; create minimal reproduction when needed.

For provider agent platforms, creative model APIs, map/geospatial dependencies and mail delivery/template/server tooling, inspect current product stage, docs, capabilities, license/usage policies and release notes before upgrade/production automation. Learned command/model/limit/provider assumptions must not be treated as permanent.
