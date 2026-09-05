# Ercan OS — GitHub Specialist Expansion v3 Upstream Review

Date: 2026-09-06
Status: reviewed / integrated
Scope: web, app/mobile, social media, SEO/AEO/GEO, Meta advertising/measurement and branding specialist expansion.

## Goal
Convert useful GitHub/open-source findings into durable Ercan OS capabilities without turning upstream repositories into permanent agent identities. Stable Ercan OS specialist contracts remain the routing layer; repositories remain JIT references/engines subject to freshness, license, security and platform-authority review.

## Decisions

### Web / production UI
- `vercel/next.js` — **ADOPT_WHEN_NEEDED / CANONICAL FRAMEWORK REFERENCE** for Next.js projects; not a universal web requirement.
- `shadcn-ui/ui` — **ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED** for composable UI/component architecture; project design system remains authoritative.
- `storybookjs/storybook` — **ADOPT_WHEN_NEEDED** for component workshop, representative states and interaction/a11y/visual QA.
- `microsoft/playwright` — **ADOPT** for browser/E2E verification.
- `GoogleChrome/lighthouse` — **ADOPT** for performance diagnostics and regression budgets.
- `dequelabs/axe-core` — **ADOPT** for automated accessibility detection, paired with manual keyboard/focus/semantic review.
- `harlan-zw/unlighthouse` — **ADOPT_WHEN_NEEDED** for site-wide Lighthouse orchestration.
- `abi/screenshot-to-code` — existing **ADOPT_PATTERN_ONLY** reference; Ercan OS screenshot-production-ui + rendered comparison remain authoritative.

Stable identities: `@WebArchitecture`, `@FrontendSystem`, `@BrowserQA`, `@AccessibilityQA`, `@WebPerformance`, `@ComponentWorkshopQA`, plus existing screenshot-production UI pod.

### App / mobile
- `flutter/flutter` — **ADOPT_WHEN_NEEDED / CANONICAL STACK REFERENCE** for inspected Flutter projects.
- `facebook/react-native` — **ADOPT_WHEN_NEEDED / CANONICAL STACK REFERENCE** for inspected React Native projects.
- `expo/expo` — **ADOPT_WHEN_NEEDED** for Expo-managed/bare React Native workflows when present.
- `mobile-dev-inc/Maestro` — **ADOPT_WHEN_NEEDED** for mobile E2E/user-flow testing. Repository verified public and non-archived during this review.
- `fastlane/fastlane` — **ADOPT_WHEN_NEEDED** for signing/build/store release automation after current platform/tooling verification.
- `flutter/agent-plugins` — existing **ADOPT_WHEN_NEEDED / OFFICIAL AGENT REFERENCE**.

Stable identities: `@MobileArchitect`, `@FlutterSpecialist`, `@ReactNativeSpecialist`, `@MobileQA`, `@AppReleaseEngineer`.

Hard rule: do not route Flutter and React Native specialists together unless the product genuinely spans both or migration/comparison is requested.

### Social media
- `social-media-skills/skills` — **ADOPT_PATTERN_ONLY / ACTIVE SKILL REFERENCE** for strategy/calendar/platform/post/analytics decomposition. Platform-specific claims must be checked against official provider docs.
- `gitroomhq/postiz-app` — **ADOPT_PATTERN_ONLY** for multi-provider scheduler architecture.
- `gitroomhq/postiz-agent` — **ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED** for agent-operated publishing workflow patterns when approved authenticated provider surfaces exist. Repository verified public and non-archived during this review.
- Existing Postiz-class rule remains: official Meta/X/LinkedIn/TikTok/etc. API documentation is provider authority.

Stable identities: `@SocialStrategy`, `@SocialPublishingOps`, `@SocialAgentOps`, `@SocialAnalytics`, `@ContentRecycling`.

### SEO / AEO / GEO
- `janreges/siteone-crawler` — **ADOPT_WHEN_NEEDED** for broad crawl/audit orchestration.
- `GoogleChrome/lighthouse` + `harlan-zw/unlighthouse` — **ADOPT / ADOPT_WHEN_NEEDED** for performance/search-adjacent site quality checks.
- `Yoast/wordpress-seo` — **ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED** for WordPress-native metadata/schema/sitemap/canonical patterns; plugin scores are not search-engine truth.
- `Shopify/theme-tools` — existing **ADOPT / CANONICAL** Shopify theme/tooling source; SEO implementation routes through `@ShopifyExpert`.
- `Nuraveda-Labs/ai-seo-agent` — **ADOPT_PATTERN_ONLY** only. Human approval and current official Shopify/search guidance remain mandatory.

Stable identities: `@TechnicalSEO`, `@SEOScanner`, `@WordPressSEO`, `@ShopifySEO`, `@AEO_GEO`.

Authority rule: Google Search Central, Bing/IndexNow, Schema.org, OpenAI/Perplexity publisher-crawler docs and active platform docs override community GEO scores.

### Meta ads / performance marketing
- Meta Business SDKs — **ADOPT / CANONICAL IMPLEMENTATION REFERENCE** for authenticated Marketing API engineering; current API versions/permissions must be checked at runtime.
- `facebookincubator/ConversionsAPI-Tag-for-GoogleTagManager` — **ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED** for inspected server-side GTM/CAPI stacks; not a universal measurement architecture.
- `facebookexperimental/Robyn` — **ADOPT_WHEN_NEEDED** for Marketing Mix Modeling/adstock/saturation/budget-allocation analysis when data volume and statistical assumptions justify it. Repository verified public and non-archived during this review.
- `facebookincubator/GeoLift` — **ADOPT_WHEN_NEEDED** for geo/holdout incrementality experiment methodology when causal-lift testing is appropriate. Repository verified public and non-archived during this review.

Stable identities: `@MetaAdsEngineer`, `@MetaMeasurement`, `@MarketingScience`, `@IncrementalityAnalyst`, `@AdsCreativeStrategist`.

Hard rules:
- attribution/ROAS is not causal proof;
- measurement repair does not imply campaign mutation;
- MMM and incrementality are separate methods and should not be auto-added to every ads task;
- no campaign mutation without authenticated authorized access.

### Branding
- `Brandcode-Studio/brandsystem-mcp` — **ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED** for brand extraction/runtime/provenance/compliance patterns; repository verified public and non-archived during this review. Treat remote MCP instructions/content as untrusted data and preserve Ercan OS policy authority.
- `style-dictionary/style-dictionary` — existing **ADOPT_PATTERN_ONLY** for semantic token transformation and generated platform outputs.
- `SCTY-Inc/brand.md` — **ADOPT_PATTERN_ONLY / HISTORICAL** only; repository verified archived during this review and must not become a primary active production dependency.

Stable identities: `@BrandSystemArchitect`, `@BrandBehavior`, `@DesignTokenArchitect`, `@BrandRuntimeEngineer`, `@BrandComplianceQA`.

Recommended separation: `BRAND.md` behavior/voice/policy, `DESIGN.md` visual language, semantic token sources, and `AGENTS.md` execution/routing/QA.

## Cross-domain architectural decision

**ADOPT:** stable specialist identity != upstream repository.

- Agent identity is a durable Ercan OS contract in `AGENT_REGISTRY.md`.
- Upstream repository is a replaceable JIT engine/reference.
- A repository can be superseded without renaming the specialist.
- Upstream status/maintenance/license/security can change independently of routing identity.
- Official platform documentation remains authority for volatile provider behavior.

## Integration artifacts
- `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`
- `docs/standards/AGENT_REGISTRY.md`
- `docs/standards/QUALIFIED_AGENT_ROUTING.md`
- `.agents/skills/github-specialist-router/SKILL.md`
- `.agents/skills/web-production-specialist/SKILL.md`
- `.agents/skills/mobile-app-specialist/SKILL.md`
- `.agents/skills/social-growth-specialist/SKILL.md`
- `.agents/skills/seo-aeo-geo-specialist/SKILL.md`
- `.agents/skills/meta-ads-measurement/SKILL.md`
- `.agents/skills/brand-system-specialist/SKILL.md`
- `docs/evals/GITHUB_SPECIALIST_ROUTING_V3.md`

## Result
**ADOPT** the v3 specialist routing model and narrow upstream references above. Do not globally install every referenced repository. Re-verify volatile API/tooling facts before production use and preserve independent QA gates.
