# Ercan OS — GitHub Specialist v3 Gap / Upstream Hygiene Pass

Date: 2026-09-07
Status: reviewed
Scope: web, app/mobile, social media, SEO/AEO/GEO, Meta ads/measurement and branding specialist upstreams.

Purpose: refresh canonical repository identity and archive status after GitHub Specialist Expansion v3, look for material missing specialist capabilities, and avoid adding agents merely because new or popular repositories exist.

## Decision summary

- **No new stable specialist identity is required.** The current 21 Stable Core + 31 GitHub Specialist v3 Extension = 52 named stable routing identities remains sufficient.
- Two canonical repository identity drifts were found and must be corrected in active v3 surfaces.
- Two plausible gap-pass candidates were found archived and must not become new production dependencies.
- Existing visual-regression/browser and mobile-platform tooling already covers the inspected capability gaps; adding overlapping agents would reduce clarity rather than improve quality.

## Canonical rename / owner drift

### Style Dictionary
- Old historical path: `amzn/style-dictionary`.
- Current canonical repository resolved by GitHub: `style-dictionary/style-dictionary`.
- Repository is public and non-archived at review time.
- Decision: current v3 active reference remains `style-dictionary/style-dictionary` — **ADOPT_PATTERN_ONLY** for semantic token lifecycle/transforms.
- Old `amzn/style-dictionary` spelling: **SUPERSEDED / RENAMED ALIAS**. It may remain in historical dated evidence but must not be reintroduced into active v3 manifest/catalog decisions.

### AI SEO Agent
- Previous path: `Nuraveda-Labs/ai-seo-agent`.
- GitHub now resolves that repository identity to `Meshpilot-AGI/ai-seo-agent`.
- Current repository is public and non-archived at review time.
- Decision: `Meshpilot-AGI/ai-seo-agent` — **ADOPT_PATTERN_ONLY** for human-approved Shopify SEO workflow ideas; official Shopify/search authority remains primary.
- Old `Nuraveda-Labs/ai-seo-agent` spelling: **SUPERSEDED / RENAMED ALIAS**.

## Gap-pass candidates rejected as new active dependencies

### Visual regression
- `lost-pixel/lost-pixel` was verified **archived**.
- Decision: **SUPERSEDED / HISTORICAL**, do not add to active production stack.
- `garris/BackstopJS` and `reg-viz/reg-suit` were verified public/non-archived and are already represented in the broader Ercan OS visual-regression/tooling catalog.
- Existing stable identities `@BrowserQA`, `@ComponentWorkshopQA`, `@PixelMatch`, `@ProductionQA` plus Playwright/Backstop/reg-suit/pixel-diff patterns are sufficient.
- No new `@VisualRegression` stable identity is needed; visual regression remains a bounded QA capability routed to the existing QA pod.

### React Native performance
- `Shopify/react-native-performance` was verified **archived**.
- Decision: **SUPERSEDED / HISTORICAL**, do not add as a new v3 active dependency.
- Mobile performance should use current React Native/Expo/Flutter platform-native profiling and current maintained tooling selected JIT by `@MobileArchitect` / implementation specialist / performance specialist.
- No new mobile-performance stable identity is justified by this pass.

## Active/non-archived references re-verified

At review time the following inspected repositories resolved as public and non-archived:
- `mobile-dev-inc/Maestro`
- `fastlane/fastlane`
- `gitroomhq/postiz-app`
- `gitroomhq/postiz-agent`
- `social-media-skills/skills`
- `janreges/siteone-crawler`
- `Meshpilot-AGI/ai-seo-agent`
- `facebookincubator/ConversionsAPI-Tag-for-GoogleTagManager`
- `facebookexperimental/Robyn`
- `facebookincubator/GeoLift`
- `Brandcode-Studio/brandsystem-mcp`
- `style-dictionary/style-dictionary`
- `garris/BackstopJS`
- `reg-viz/reg-suit`

This review records repository identity/archive state only. It does not certify current releases, licenses, security advisories, API compatibility, account permissions or production fitness; those remain runtime verification duties.

## Social listening / analytics gap

Broad GitHub discovery for a canonical multi-provider social-listening/analytics engine did not produce a candidate strong enough to supersede provider-native APIs plus the existing `@SocialAnalytics` / `@SocialStrategy` architecture.

Decision: **NO PROMOTION**. Keep provider-native analytics as authority and use community dashboards only as task-specific patterns after provenance/permission review.

## Routing consequences

- Stable routing identity count remains **52 total = 21 Core + 31 v3 Extension**.
- Do not create duplicate specialists for visual regression or mobile performance merely to mirror a repository category.
- `@UpstreamIntelligence` must canonicalize redirects/owner transfers before writing a repo into active manifests.
- Active v3 manifest must use `style-dictionary/style-dictionary` and `Meshpilot-AGI/ai-seo-agent`.
- Historical aliases may appear only in explicit superseded/rename notes or dated evidence.
- Archived `lost-pixel/lost-pixel` and `Shopify/react-native-performance` must not become primary active production dependencies.

## Files to update from this review

- `docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json`
- `docs/upstream/GITHUB_SPECIALIST_CATALOG_V3.md`
- `docs/upstream/UPSTREAM_INTELLIGENCE_CURRENT.md`
- `docs/standards/DISCOVERY_ADOPTION_LEDGER.md`
- `scripts/validate_github_specialist_v3.py`
- `.github/workflows/github-specialist-v3-doctor.yml`

## Adoption decision

**ADOPT — UPSTREAM HYGIENE / NO NEW AGENT.** Correct canonical names, preserve archive/rename history, and strengthen doctor regression guards without increasing the stable identity count.
