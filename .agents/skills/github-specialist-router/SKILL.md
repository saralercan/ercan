---
name: github-specialist-router
description: Route Ercan OS work across reviewed GitHub-backed specialist pods for web, app/mobile, social media, SEO/AEO/GEO, Meta ads/measurement and branding. Use when the user asks to run all agents for any of these domains, asks to add GitHub experts, or when a material task spans two or more of these domains.
---

# GitHub Specialist Router

Load `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`, root `AGENTS.md`, `docs/standards/AGENT_REGISTRY.md`, and `docs/standards/QUALIFIED_AGENT_ROUTING.md`.

## Routing rule
Treat “tüm ajanları çalıştır” as qualified routing. Select every materially relevant specialist and no unrelated specialist.

## Domain pods
- Web: `@WebArchitecture`, `@FrontendSystem`, `@ScreenshotToCode` when reference-led, `@WebPerformance`, `@AccessibilityQA`, `@BrowserQA`, `@ComponentWorkshopQA` when relevant.
- App/mobile: `@MobileArchitect`, exactly the implementation-stack specialist(s) required (`@FlutterSpecialist` and/or `@ReactNativeSpecialist`), `@MobileQA`, `@AppReleaseEngineer` only when release/build/store delivery is in scope.
- Social: `@SocialStrategy`, `@SocialPublishingOps`, `@SocialAgentOps` when authenticated agent-operated publishing is intended, `@SocialAnalytics`, `@ContentRecycling` when cross-channel reuse is required.
- SEO/AEO/GEO: `@TechnicalSEO`, `@SEOScanner`, platform specialist (`@WordPressSEO`/`@ShopifySEO`) when applicable, `@AEO_GEO` when answer-engine/AI-discovery is material.
- Meta ads: `@MetaAdsEngineer`, `@MetaMeasurement`, `@MarketingScience`, `@IncrementalityAnalyst`, `@AdsCreativeStrategist` according to the actual campaign/measurement question.
- Branding: `@BrandSystemArchitect`, `@BrandBehavior`, `@DesignTokenArchitect`, `@BrandRuntimeEngineer`, independent `@BrandComplianceQA` as material.

## Procedure
1. Detect project, repository, platform, brand and production constraints.
2. Decompose the task into domain capabilities rather than keywords.
3. Select the smallest sufficient pod; add Upstream Intelligence only for a real tooling/current-source gap or explicit GitHub research.
4. Load the matching domain skill from this expansion.
5. Route implementation through platform experts where applicable.
6. Preserve authentication/approval boundaries for publishing and ads.
7. Require independent QA for material implementation.
8. Report `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT VERIFIED` based on executed evidence, never agent-count theater.

## Output
Selected pod, task boundaries, dependencies, execution evidence, QA outcome and completion state.
