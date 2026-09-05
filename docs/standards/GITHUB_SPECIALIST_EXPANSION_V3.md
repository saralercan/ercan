# Ercan OS — GitHub Specialist Expansion v3

Status: active
Date: 2026-09-06

Purpose: promote reviewed GitHub/open-source capabilities into qualified Ercan OS specialist routing for web, app/mobile, social media, SEO/AEO/GEO, Meta advertising/measurement and branding. This standard supplements, and never overrides, root `AGENTS.md`, `AGENT_REGISTRY.md`, `QUALIFIED_AGENT_ROUTING.md`, project adapters, safety, scope and independent QA rules.

## Core rule

GitHub repositories are upstream capability references, not autonomous authorities. Stable Ercan OS specialist identities own the task. Upstreams are loaded JIT, re-verified when volatile, and adopted narrowly. Archived/deprecated projects are historical/pattern references only unless a maintained successor does not exist and the task explicitly justifies them.

When the user says “tüm ajanları çalıştır”, Orchestrator must include every materially relevant specialist from the pods below, but must not fan out unrelated domains merely to increase agent count.

## Web / production UI pod

Stable specialists:
- `@WebArchitecture` — modern full-stack web architecture, routing/data/cache/rendering boundaries, deployment fit and native framework patterns.
- `@FrontendSystem` — reusable component system, shadcn/ui-style composition, Storybook/component workshop, shared state and design-system implementation.
- `@ScreenshotToCode` — existing reference-led implementation specialist; preserve current `screenshot-production-ui` contract.
- `@BrowserQA` — Playwright-based Chromium/Firefox/WebKit E2E and runtime verification.
- `@AccessibilityQA` — axe-core-assisted accessibility checks plus manual keyboard/focus/semantic review.
- `@WebPerformance` — Lighthouse/Core Web Vitals/performance-budget work; site-wide audits may use Unlighthouse.
- `@ComponentWorkshopQA` — Storybook representative states, component interaction/a11y/visual checks where a component workshop exists.

Reviewed upstream references:
- `vercel/next.js`
- `shadcn-ui/ui`
- `storybookjs/storybook`
- `microsoft/playwright`
- `GoogleChrome/lighthouse`
- `dequelabs/axe-core`
- `harlan-zw/unlighthouse`
- `abi/screenshot-to-code` as a reference pattern; Ercan OS fidelity/QA rules remain authoritative.

Minimum material web flow:
`@WebArchitecture → platform specialist when applicable → @FrontendSystem → implementation → @WebPerformance/@AccessibilityQA as risk requires → @BrowserQA → independent QA`.

## App / mobile pod

Stable specialists:
- `@MobileArchitect` — chooses and governs Flutter vs React Native/Expo or another verified native path based on product/runtime constraints.
- `@FlutterSpecialist` — Flutter/Dart implementation, platform integration, responsive/adaptive UI and build correctness.
- `@ReactNativeSpecialist` — React Native/Expo implementation, native-module boundaries and platform behavior.
- `@MobileQA` — Maestro-centered mobile E2E flows plus platform-native checks when required.
- `@AppReleaseEngineer` — signing/build/release automation, store metadata/screenshots and CI/release safety; Fastlane is an upstream reference when appropriate.

Reviewed upstream references:
- `flutter/flutter`
- `facebook/react-native`
- `expo/expo`
- `mobile-dev-inc/Maestro`
- `fastlane/fastlane`
- official Flutter agent/plugin sources already tracked by Upstream Intelligence when agent-oriented Flutter support is needed.

Do not select both Flutter and React Native specialists unless the project actually spans both or a migration/comparison is requested.

## Social media pod

Stable specialists:
- `@SocialStrategy` — audience, platform strategy, content pillars, hooks, calendar, format and growth hypotheses.
- `@SocialPublishingOps` — provider-neutral scheduling/publishing architecture, approvals, media state, retries, idempotency and reconciliation.
- `@SocialAgentOps` — agent-operated social workflows when an approved publishing surface/API exists; never bypass account permissions or approval boundaries.
- `@SocialAnalytics` — content/channel performance, retention/watch-time where available, saves/shares/clicks/conversions and iteration recommendations.
- `@ContentRecycling` — transforms validated source content across channels while preserving brand truth and avoiding low-value duplication.

Reviewed upstream references:
- `social-media-skills/skills` — active skill decomposition/reference source; verify platform-specific claims against official provider docs.
- `gitroomhq/postiz-app` — provider/scheduler architecture reference.
- `gitroomhq/postiz-agent` — agent-operated social workflow reference.

Official Meta/X/LinkedIn/TikTok/etc. provider documentation remains authority for permissions, API behavior, limits and publishing semantics.

## SEO / AEO / GEO pod

Stable specialists:
- `@TechnicalSEO` — crawl/index controls, canonical, metadata, headings, internal links, robots, sitemap, hreflang, structured data and technical search hygiene.
- `@SEOScanner` — site-wide crawl/audit orchestration using the smallest suitable combination of SiteOne Crawler, Lighthouse/Unlighthouse and platform-native tools.
- `@WordPressSEO` — WordPress-native metadata/schema/sitemap/canonical/indexability practices; route implementation through `@WordPressExpert`.
- `@ShopifySEO` — Shopify-native technical SEO, Liquid/theme constraints, product/feed/entity consistency; route implementation through `@ShopifyExpert`.
- `@AEO_GEO` — answer-engine/AI-discovery eligibility, structured answerability, entity consistency, crawler accessibility and evidence-based AI-search measurement.

Reviewed upstream references:
- `janreges/siteone-crawler`
- `GoogleChrome/lighthouse`
- `harlan-zw/unlighthouse`
- `Yoast/wordpress-seo`
- `Shopify/theme-tools`
- `Nuraveda-Labs/ai-seo-agent` — community pattern only; human approval and official Shopify/search guidance remain mandatory.

Authority rule: Google Search Central, Bing/IndexNow, Schema.org, OpenAI/Perplexity publisher/crawler documentation and official platform docs override community GEO/SEO scoring repos.

## Meta ads / performance marketing pod

Stable specialists:
- `@MetaAdsEngineer` — Meta Marketing API/Business SDK campaign, ad set, ad, creative, account and insights engineering where authenticated access exists.
- `@MetaMeasurement` — Pixel + Conversions API/server-side event architecture, event matching, deduplication, diagnostics and conversion measurement.
- `@MarketingScience` — channel efficiency, adstock, saturation, Marketing Mix Modeling and budget-allocation analysis.
- `@IncrementalityAnalyst` — geo/holdout/incrementality experiment design and interpretation; distinguishes attribution from causal lift.
- `@AdsCreativeStrategist` — offer/message/audience/creative-test design linked to measurement, not vanity metrics.

Reviewed upstream references:
- `facebook/facebook-nodejs-business-sdk` and/or official Meta Business SDK equivalents.
- `facebookincubator/ConversionsAPI-Tag-for-GoogleTagManager` as an upstream implementation reference when still appropriate to the inspected stack.
- `facebookexperimental/Robyn` for MMM methodology/tooling when statistically justified.
- `facebookincubator/GeoLift` for geo-experiment/incrementality methodology when appropriate.

Hard rules:
- never claim causal lift from ROAS/attribution alone;
- do not mutate campaigns without authenticated authorized access and the task requiring it;
- separate campaign execution, measurement, MMM and incrementality responsibilities;
- verify current Meta API versions/permissions from official sources at runtime.

## Branding pod

Stable specialists:
- `@BrandSystemArchitect` — converts brand strategy, identity, audience, voice and usage rules into an operational cross-channel system.
- `@BrandBehavior` — defines voice, message hierarchy, audience behavior, do/don’t, escalation and channel behavior in machine-readable/project-readable form.
- `@DesignTokenArchitect` — semantic color/type/spacing/radius/motion tokens and generated web/iOS/Android outputs; generated derivatives are not hand-edited.
- `@BrandRuntimeEngineer` — compiles approved brand sources into reusable agent/runtime context and provenance-aware artifacts.
- `@BrandComplianceQA` — independently verifies web/app/social/ad outputs against brand rules, exact assets, copy constraints and channel requirements.

Reviewed upstream references:
- `Brandcode-Studio/brandsystem-mcp` — active upstream reference for brand-system extraction/runtime patterns; review provenance, permissions and output before production adoption.
- `style-dictionary/style-dictionary` — token transformation/output reference.
- `SCTY-Inc/brand.md` — archived as of this review; `ADOPT_PATTERN_ONLY/HISTORICAL`, never the primary active production dependency.

Recommended separation:
- `BRAND.md` — behavior, voice, audience, message and brand-policy layer.
- `DESIGN.md` — visual/composition/typography/imagery layer when the project uses such a file.
- design tokens — semantic machine-readable visual values.
- `AGENTS.md` — working/routing/QA instructions; it must not become the brand book.

## Qualified routing matrix

For a material website task, consider web architecture/frontend/platform + technical SEO + performance + accessibility + browser QA when those surfaces are touched.
For a material mobile task, select `@MobileArchitect`, exactly the implementation stack specialist(s) required, `@MobileQA`, and release engineering only when build/store delivery is in scope.
For social work, separate strategy, production/publishing and analytics; authenticated publishing is never implied by content creation.
For SEO, select platform SEO specialist only when that platform is active; add AEO/GEO only when AI-discovery/search-answerability is in scope or materially affected.
For Meta advertising, campaign engineering, measurement, marketing science and incrementality are separate capabilities and are selected independently.
For branding, brand system/token/runtime specialists are included when cross-channel or reusable identity consistency is materially affected; `@BrandComplianceQA` remains independent of implementation.

## Cross-domain examples

### Premium Shopify storefront + SEO + Meta measurement
`@Orchestrator → @ShopifyExpert → @WebArchitecture/@FrontendSystem as needed → @ShopifySEO/@TechnicalSEO → @WebPerformance/@AccessibilityQA → @BrowserQA → @MetaMeasurement → independent QA`.

### Reference-led WordPress rebuild
`@Orchestrator → @WordPressExpert → @ScreenshotToCode → @RealAsset → @PixelMatch → @TechnicalSEO → @WebPerformance/@AccessibilityQA → @BrowserQA/@ProductionQA`.

### Mobile guide app + brand system
`@Orchestrator → @MobileArchitect → @FlutterSpecialist or @ReactNativeSpecialist → @DesignTokenArchitect/@BrandSystemArchitect → @MobileQA → @BrandComplianceQA`.

### Social campaign with paid Meta layer
`@Orchestrator → @BrandSystemArchitect/@SocialStrategy → creative specialists → @AdsCreativeStrategist → @MetaAdsEngineer when execution access exists → @MetaMeasurement → @SocialAnalytics/@MarketingScience as appropriate → Brand/measurement QA`.

## Completion gate

A task using this expansion can be marked `VERIFIED` only when:
- selected specialists were actually required and actually executed as workstreams/capabilities available in the runtime;
- platform/provider authority was checked for volatile behavior;
- implementation and independent QA are separated for material changes;
- no archived/community repository was silently elevated above a maintained official/canonical upstream;
- no unavailable write/auth capability was implied;
- the user’s do-not-touch, brand, scope and production constraints propagated across handoffs.
