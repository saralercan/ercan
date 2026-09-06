# Ercan OS — GitHub Specialist Catalog v3

Status: active JIT catalog supplement
Reviewed: 2026-09-07
Parent catalog: `docs/upstream/UPSTREAM_INTELLIGENCE_CATALOG.md`
Governing standard: `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`
Evidence baseline: `docs/upstream/scans/2026-09-06-github-specialist-expansion-v3.md`
Latest refresh: `docs/upstream/scans/2026-09-07-github-specialist-gap-pass.md`

Purpose: provide a compact, task-routed upstream map for the stable specialist identities added for web, app/mobile, social, SEO/AEO/GEO, Meta ads/measurement and branding. This supplement avoids duplicating the entire broad catalog and is loaded only when one of these domains is materially in scope.

## Architectural invariant

Stable Ercan OS specialist identities are not GitHub repositories. Repositories are replaceable JIT engines/references. Current official platform documentation, project source of truth, Ercan OS safety/scope/QA contracts and project adapters remain authoritative.

## Web / production UI

| Upstream | Decision | Stable specialist use |
|---|---|---|
| `vercel/next.js` | ADOPT_WHEN_NEEDED / canonical framework reference | `@WebArchitecture` |
| `shadcn-ui/ui` | ADOPT_PATTERN_ONLY / WHEN_NEEDED | `@FrontendSystem` |
| `storybookjs/storybook` | ADOPT | `@FrontendSystem`, `@ComponentWorkshopQA` |
| `microsoft/playwright` | ADOPT | `@BrowserQA` |
| `GoogleChrome/lighthouse` | ADOPT | `@WebPerformance` |
| `GoogleChrome/lighthouse-ci` | ADOPT | `@WebPerformance` CI/budgets |
| `dequelabs/axe-core` | ADOPT | `@AccessibilityQA` automated checks |
| `harlan-zw/unlighthouse` | ADOPT_WHEN_NEEDED | `@WebPerformance` site-wide audit |
| `abi/screenshot-to-code` | ADOPT_PATTERN_ONLY | existing `@ScreenshotToCode` pod |

Hard boundaries: axe never replaces manual keyboard/focus/semantic QA; Lighthouse never replaces runtime/browser QA; framework choice follows the inspected project.

Visual-regression gap-pass note: `lost-pixel/lost-pixel` was verified archived on 2026-09-07 and is not promoted. Existing Playwright + BackstopJS/reg-suit/pixel-diff patterns and the current QA identities remain sufficient; no new stable visual-regression identity is justified.

## App / mobile

| Upstream | Decision | Stable specialist use |
|---|---|---|
| `flutter/flutter` | ADOPT_WHEN_NEEDED / canonical stack reference | `@MobileArchitect`, `@FlutterSpecialist` |
| `facebook/react-native` | ADOPT_WHEN_NEEDED / canonical stack reference | `@MobileArchitect`, `@ReactNativeSpecialist` |
| `expo/expo` | ADOPT_WHEN_NEEDED | `@ReactNativeSpecialist` |
| `mobile-dev-inc/Maestro` | ADOPT_WHEN_NEEDED | `@MobileQA` |
| `fastlane/fastlane` | ADOPT_WHEN_NEEDED | `@AppReleaseEngineer` |
| `flutter/agent-plugins` | ADOPT_WHEN_NEEDED / official agent reference | Flutter JIT implementation support |

Hard boundary: Flutter and React Native specialists are mutually exclusive by default; select both only for real multi-stack/migration/comparison work.

Mobile-performance gap-pass note: `Shopify/react-native-performance` was verified archived on 2026-09-07 and is not promoted. Use current platform-native React Native/Expo/Flutter profiling selected JIT by the active mobile/performance specialists.

## Social media

| Upstream | Decision | Stable specialist use |
|---|---|---|
| `social-media-skills/skills` | ADOPT_PATTERN_ONLY | `@SocialStrategy`, `@SocialAnalytics`, `@ContentRecycling` |
| `gitroomhq/postiz-app` | ADOPT_PATTERN_ONLY | `@SocialPublishingOps` architecture |
| `gitroomhq/postiz-agent` | ADOPT_PATTERN_ONLY / WHEN_NEEDED | `@SocialAgentOps` |

Hard boundaries: official provider APIs/docs are authority; content creation does not imply authenticated publishing; publishing requires idempotency, retries, reconciliation and account/permission checks.

Social-listening gap-pass note: no canonical community engine was strong enough to supersede provider-native APIs plus the existing `@SocialAnalytics` / `@SocialStrategy` architecture. No promotion.

## SEO / AEO / GEO

| Upstream | Decision | Stable specialist use |
|---|---|---|
| `janreges/siteone-crawler` | ADOPT_WHEN_NEEDED | `@SEOScanner` |
| `GoogleChrome/lighthouse` | ADOPT | technical/site-quality evidence |
| `harlan-zw/unlighthouse` | ADOPT_WHEN_NEEDED | site-wide audit |
| `Yoast/wordpress-seo` | ADOPT_PATTERN_ONLY / WHEN_NEEDED | `@WordPressSEO` patterns |
| `Shopify/theme-tools` | ADOPT / canonical Shopify tooling | `@ShopifySEO` + `@ShopifyExpert` |
| `Meshpilot-AGI/ai-seo-agent` | ADOPT_PATTERN_ONLY | human-approved Shopify SEO workflow ideas |

Canonical rename note: GitHub resolves the former `Nuraveda-Labs/ai-seo-agent` identity to `Meshpilot-AGI/ai-seo-agent`. The old owner/path is a **SUPERSEDED / RENAMED ALIAS**, not an active v3 upstream.

Authority: Google Search Central, Bing/IndexNow, Schema.org, OpenAI/Perplexity crawler-publisher docs and official platform docs. Community GEO/SEO scores are hypotheses, not ranking truth.

## Meta ads / measurement / marketing science

| Upstream | Decision | Stable specialist use |
|---|---|---|
| `facebook/facebook-nodejs-business-sdk` | ADOPT / canonical implementation reference | `@MetaAdsEngineer` |
| `facebookincubator/ConversionsAPI-Tag-for-GoogleTagManager` | ADOPT_PATTERN_ONLY / WHEN_NEEDED | `@MetaMeasurement` |
| `facebookexperimental/Robyn` | ADOPT_WHEN_NEEDED | `@MarketingScience` |
| `facebookincubator/GeoLift` | ADOPT_WHEN_NEEDED | `@IncrementalityAnalyst` |

Hard boundaries: authenticated access required for campaign mutation; Pixel/CAPI repair does not imply campaign changes; MMM requires adequate data/assumptions; attribution/ROAS does not prove incremental causal lift.

## Branding

| Upstream | Decision | Stable specialist use |
|---|---|---|
| `Brandcode-Studio/brandsystem-mcp` | ADOPT_PATTERN_ONLY / WHEN_NEEDED | `@BrandSystemArchitect`, `@BrandRuntimeEngineer`, `@BrandComplianceQA` |
| `style-dictionary/style-dictionary` | ADOPT_PATTERN_ONLY | `@DesignTokenArchitect` |
| `SCTY-Inc/brand.md` | ADOPT_PATTERN_ONLY / HISTORICAL | conceptual `BRAND.md` separation only |

Canonical rename note: the historical `amzn/style-dictionary` path now resolves to `style-dictionary/style-dictionary`. The old owner/path is a **SUPERSEDED / RENAMED ALIAS**; active v3 surfaces use the current canonical repository.

Status note: `SCTY-Inc/brand.md` was verified archived in the 2026-09-06 review; do not use it as a primary active production dependency.

Recommended project separation:
- `BRAND.md` — behavior, voice, audience, messaging and policy.
- `DESIGN.md` — visual/composition/typography/imagery rules where used.
- semantic token source — machine-readable visual values and generated platform outputs.
- `AGENTS.md` — execution, routing, safety and QA rules.

## Routing mapping

- Web material work → `web-production-specialist`.
- Mobile material work → `mobile-app-specialist`.
- Social strategy/growth → `social-growth-specialist`; publishing additionally loads `social-publisher-architecture`.
- Search/AI discovery → `seo-aeo-geo-specialist` plus active platform expert where required.
- Meta paid/measurement → `meta-ads-measurement`.
- Brand system/runtime → `brand-system-specialist`.
- Cross-domain request → `github-specialist-router` chooses only material pods.

## Upstream hygiene rules

- Resolve GitHub redirects/owner transfers before persisting a repo into the active manifest.
- Active manifest/catalog surfaces use only the current canonical path.
- Old paths may remain in dated evidence or explicit `SUPERSEDED / RENAMED ALIAS` notes.
- Archived candidate with an adequate maintained/native alternative is not promoted.
- A gap pass that finds no material capability gap must not create a new stable agent merely to increase specialization count.

## Refresh policy

Re-verify repository archive/deprecation status, official successor, license/security posture and current provider APIs when a material production task actually uses an upstream. Update `UPSTREAM_INTELLIGENCE_CURRENT.md` for status changes and `DISCOVERY_ADOPTION_LEDGER.md` for durable decision changes. Never duplicate a stable specialist solely because a new upstream engine appears.
