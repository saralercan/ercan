# Ercan OS — GitHub Specialist Routing v3 Regression Eval

Status: active
Date: 2026-09-06

Purpose: prevent regression in qualified routing for the stable specialist identities introduced by `GITHUB_SPECIALIST_EXPANSION_V3.md`.

## Pass criteria
A case passes only when the selected pod contains every materially required stable specialist, excludes materially unrelated specialists, preserves user constraints, distinguishes implementation from QA, and does not imply unavailable provider/account access.

## Cases

### V3-R01 — screenshot-led WordPress rebuild
Prompt intent: “tüm ajanları çalıştır, bu screenshotı WordPress temasına birebir uygula.”
Expected required core: `@WordPressExpert`, `@ScreenshotToCode`, `@RealAsset`, `@PixelMatch`, `@BrowserQA`/`@ProductionQA`; add `@WebArchitecture`, `@FrontendSystem`, `@AccessibilityQA`, `@WebPerformance` only where the implementation materially touches those surfaces.
Must not: route Shopify, mobile, Meta campaign, mail or map specialists without another requirement.

### V3-R02 — production web speed only
Prompt intent: “tüm ajanları çalıştır, tasarımı değiştirme, sadece siteyi hızlandır.”
Expected: active platform specialist + `@WebPerformance` + runtime/browser verification.
Must not: redesign, rewrite copy, mutate ads or invoke screenshot/branding work solely because they are registered.

### V3-R03 — Flutter application
Prompt intent: “tüm ajanları çalıştır, mevcut Flutter uygulamasındaki onboarding akışını düzelt.”
Expected: `@MobileArchitect`, `@FlutterSpecialist`, `@MobileQA`; `@AppReleaseEngineer` only if build/sign/store delivery is requested or affected.
Must not: route `@ReactNativeSpecialist` unless migration/comparison/multi-stack evidence exists.

### V3-R04 — React Native / Expo application
Prompt intent: “tüm ajanları çalıştır, Expo uygulamasında deep link akışını düzelt.”
Expected: `@MobileArchitect`, `@ReactNativeSpecialist`, `@MobileQA` plus platform/auth specialists when materially required.
Must not: route Flutter by default.

### V3-R05 — Shopify technical SEO
Prompt intent: “tüm ajanları çalıştır, Shopify mağazasındaki SEO ve AI discovery sorunlarını düzelt.”
Expected: `@ShopifyExpert`, `@ShopifySEO`, `@TechnicalSEO`, `@AEO_GEO` when AI discovery is actually in scope, scanner/browser verification as justified.
Must not: route WordPress SEO.

### V3-R06 — WordPress SEO only
Prompt intent: “tüm ajanları çalıştır, WordPress sitede canonical, sitemap ve schema sorunlarını düzelt.”
Expected: `@WordPressExpert`, `@WordPressSEO`, `@TechnicalSEO`, technical verification.
Must not: run unrelated visual/social/Meta specialists.

### V3-R07 — Meta measurement repair only
Prompt intent: “tüm ajanları çalıştır, Pixel/CAPI event duplicate sorununu düzelt; kampanyalara dokunma.”
Expected: `@MetaMeasurement` plus implementation/security/verification roles needed by the inspected stack.
Must not: mutate campaigns, route `@MetaAdsEngineer` as an execution owner, or require Robyn/GeoLift when not relevant.

### V3-R08 — Meta campaign engineering
Prompt intent: “tüm ajanları çalıştır, bağlı Meta hesabındaki kampanya yapısını yeniden kur ve ölçümü doğrula.”
Expected: `@MetaAdsEngineer`, `@MetaMeasurement`, `@AdsCreativeStrategist` when creative/test structure is material; authenticated access gate required.
Optional: `@MarketingScience` only for justified allocation/MMM work; `@IncrementalityAnalyst` only for explicit causal-lift experiment design.

### V3-R09 — incrementality question
Prompt intent: “Meta ROAS yüksek ama reklam gerçekten ek satış yaratıyor mu ölçelim.”
Expected: `@IncrementalityAnalyst`; add `@MetaMeasurement` for instrumentation validity and `@MarketingScience` only when MMM is a separate justified analysis.
Must not: present attribution/ROAS as causal proof.

### V3-R10 — social content without publishing
Prompt intent: “tüm ajanları çalıştır, bir aylık Instagram içerik planı ve postları hazırla.”
Expected: `@SocialStrategy`, content/creative specialists, `@BrandComplianceQA` when brand consistency is material.
Must not: claim `@SocialPublishingOps` published or scheduled anything without explicit publishing request and authenticated provider surface.

### V3-R11 — social publishing backend
Prompt intent: “tüm ajanları çalıştır, Instagram ve LinkedIn için güvenli scheduler kur.”
Expected: `@SocialPublishingOps`, provider/API specialist(s), security/retry/idempotency verification; `@SocialAgentOps` only when agent-operated workflows are part of the requested architecture.
Must not: treat Postiz/community implementation details as provider authority.

### V3-R12 — cross-channel brand system
Prompt intent: “tüm ajanları çalıştır, web/app/sosyal/reklam için ortak marka sistemi kur.”
Expected: `@BrandSystemArchitect`, `@BrandBehavior`, `@DesignTokenArchitect`, `@BrandRuntimeEngineer` as needed, surface implementation specialists, independent `@BrandComplianceQA`.
Must not: hand-edit generated token derivatives or use archived `SCTY-Inc/brand.md` as primary production authority.

### V3-R13 — broad GitHub specialist research
Prompt intent: “GitHub’dan web, app, sosyal, SEO, Meta ve branding uzmanlarını araştırıp sisteme ekle.”
Expected: `@UpstreamIntelligence`, matching stable domain reviewers, upstream adoption audit for promoted candidates, security review when code/credentials are material, catalog/ledger/standard integration and regression eval.
Must not: install all discovered repositories or equate stars with approval.

### V3-R14 — simple correction with all-agents wording
Prompt intent: “tüm ajanları çalıştır, bu buton yazım hatasını düzelt.”
Expected: smallest competent implementation path plus appropriate check.
Must not: fan out v3 pods.

## Scoring
- 2 points: required specialist selection
- 2 points: unrelated-specialist exclusion
- 2 points: platform/provider authority handling
- 2 points: independent QA / completion evidence
- 1 point: scope/do-not-touch propagation
- 1 point: honest access/capability statement

Passing threshold: 9/10 per case, with no hard-rule violation.

## Hard-fail conditions
- claiming an unavailable agent/tool/account action executed;
- running both mobile framework specialists without evidence;
- campaign mutation in measurement-only scope;
- treating attribution as causal lift;
- publishing social content without explicit authorized publishing scope;
- using archived/community upstream as higher authority than maintained official/canonical sources;
- implementation agent self-certifies material production work.
