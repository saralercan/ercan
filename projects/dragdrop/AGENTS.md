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
- Drag&Drop customer/designer/brand email routes through `@DragDropCustomerService` + `@DragDropMailAgent`; it must load `docs/standards/DRAGDROP_MAIL_AGENT.md` and the locked `docs/standards/DRAGDROP_MAIL_CANONICAL_TEMPLATE.html` before rendering HTML.
- Türkiye-based brand/designer mail defaults to Turkish; canonical B2B/PANEL CTA styling and exact same-thread/approval/post-send QA rules are mandatory.
- Notification-template changes preserve current Shopify variables/localization and are preview/tested before live use.

## Project memory priority
`projects/dragdrop/PROJECT.md` → current task evidence → project decision/correction logs → general standards.

Completion: `VERIFIED` only after required implementation + independent browser/visual/search/measurement/mail QA pass for the surfaces actually touched.

## Web Builder Capability Pack
For material storefront generation/modernization, visual editing, localization, media optimization, PWA/offline, frontend-health, browser-operator or web-security work, load `.agents/skills/web-builder-capability-pack/SKILL.md`. Keep `@ShopifyExpert` as the platform owner. Use ShopifyStorefront/HeadlessCommerce lanes only when the inspected task requires them; Hydrogen is not a default. WordPress lanes do not apply to DragDrop unless a separate verified WordPress surface is explicitly introduced.


## Customer service & mail runtime

For any customer/designer/brand/partner communication task, load `docs/standards/DRAGDROP_MAIL_AGENT.md` and `.agents/skills/dragdrop-mail-agent/SKILL.md`.

Runtime owners:
- `Drag&Drop Müşteri Temsilcisi Ajanı` — inbound context, intent, onboarding, product-intake and truthful operational response.
- `Drag&Drop Mail Ajanı` — Gmail drafting/execution, same-thread reply integrity and post-send evidence.

Canonical product onboarding workbook:
`DragDrop_Standart_Urun_Yukleme_Sablonu.xlsx`

Product photos are supplied separately through Google Drive or WeTransfer, with filenames mapped to SKU/product code.

Same-thread rule:
- read the full Gmail thread;
- show the production draft to the user;
- require explicit approval before real send;
- use the actual inbound Gmail message id as `reply_message_id`;
- verify SENT, raw From = `Drag&Drop <info@draganddrop.tr>`, BCC empty and thread id integrity.

When `tüm ajanları çalıştır` or equivalent is used on a relevant Drag&Drop mail/customer task, both runtime agents are mandatory members of the qualified ACTIVE pod with `@DragDrop` and independent mail QA.
