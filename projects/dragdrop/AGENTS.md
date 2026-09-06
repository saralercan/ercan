# @DragDrop — Project Adapter

Inherit repository root `AGENTS.md`, `docs/standards/AGENT_ENGINEERING.md`, `PLATFORM_ENGINEERING.md`, `MAIL_ENGINEERING.md` when mail is relevant, `BRAND_SOCIAL.md` when relevant, `UPSTREAM_TOOLCHAIN.md`, and `GITHUB_SPECIALIST_EXPANSION_V3.md` + `github-specialist-router` for material web/social/SEO/Meta/branding work.

## Canonical project
- Storefront: https://www.draganddrop.tr/
- Customer/designer application surfaces may use `draganddrop.online` where the live site links there.
- Platform: Shopify storefront/e-commerce. Do **not** route this project through WordPress/Hostinger rules unless a separate explicitly named sub-system actually uses them.

## Primary role
`@DragDrop` project owner + `@ShopifyExpert` platform owner with qualified v3 specialist pods and independent QA.

## GitHub Specialist v3 project routing

These are candidate pods, not literal fan-out. Select only specialists with material contribution.

- **Storefront UI / shared frontend / speed / accessibility:** `@FrontendSystem`, `@WebPerformance`, `@AccessibilityQA`, `@BrowserQA`; add screenshot-production specialists when a visual reference is authoritative.
- **SEO / AI discovery:** `@ShopifySEO`, `@TechnicalSEO`, `@SEOScanner`, `@AEO_GEO` according to crawl/platform/AI-discovery scope.
- **Brand/design system:** `@DesignTokenArchitect`, independent `@BrandComplianceQA` when shared visual contracts or cross-channel brand consistency are materially affected.
- **Social:** `@SocialStrategy`, `@SocialPublishingOps`, `@SocialAnalytics` only for actual social strategy/publishing/measurement tasks. Content creation does not imply authenticated publishing.
- **Meta ads / measurement:** `@AdsCreativeStrategist`, `@MetaAdsEngineer`, `@MetaMeasurement`, `@MarketingScience`, `@IncrementalityAnalyst` independently according to execution, instrumentation, allocation/MMM or causal-lift scope. Measurement-only tasks must not mutate campaigns.

The machine-readable candidate map is `docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json` under `project_routing.dragdrop`.

## Non-negotiable project behavior
- Inspect current live/theme state before edits.
- Shopify-native sections/blocks/snippets/templates/app extensions first; no brittle storefront DOM hacks when native extension surfaces exist.
- Preserve merchant-editable Theme Editor behavior.
- Never invent product/designer/price/discount data.
- Scope preservation is strict: requested UI/content change must not mutate unrelated logo, layout, products, collections or checkout behavior.
- Use current Shopify Theme Tools/Theme Check/CLI path; verify volatile API/CLI behavior from official Shopify sources.
- Test product/variant/cart/menu/search/account/localization flows affected by the change.
- Critical mobile QA includes overlap, overflow, drawer/menu stacking, dock/header collision and tap targets.
- Material storefront UI work normally includes `@WebPerformance`, `@AccessibilityQA` and `@BrowserQA` when those surfaces can regress, even if the user did not name them.
- Publish only after preview/development-theme verification and with a known rollback point.
- Shopify-owned order/account/customer notifications remain platform-native unless a custom app/backend workflow materially requires another mail transport.
- Do not send mail from storefront Liquid/JS. B2B/designer/custom workflow mail belongs in the app/backend/service layer and follows `MAIL_ENGINEERING.md` with idempotency, safe testing and delivery-event handling as relevant.
- Notification-template changes preserve current Shopify variables/localization and are preview/tested before live use.

## Project memory priority
`projects/dragdrop/PROJECT.md` → current task evidence → project decision/correction logs → general standards.

Completion: `VERIFIED` only after required implementation + independent browser/visual/search/measurement/mail QA pass for the surfaces actually touched.
