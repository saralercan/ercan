---
name: github-specialist-router
description: Route Ercan OS work across reviewed GitHub-backed specialist pods for web, app/mobile, social media, SEO/AEO/GEO, Meta ads/measurement, branding and presentations. Use when the user asks to run all agents for any of these domains, asks to add GitHub experts, or when a material task spans two or more of these domains.
---

# GitHub Specialist Router

Load `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`, root `AGENTS.md`, `docs/standards/AGENT_REGISTRY.md`, and `docs/standards/QUALIFIED_AGENT_ROUTING.md`.

## Routing rule
Treat “tüm ajanları çalıştır” as qualified routing. Select every materially relevant specialist and no unrelated specialist.

## Domain pods
- Web: `@WebArchitecture`, `@FrontendSystem`, `@ScreenshotToCode` when reference-led, `@WebPerformance`, `@AccessibilityQA`, `@BrowserQA`, `@ComponentWorkshopQA` when relevant. For build-from-brief, autonomous/rapid/local builder, visual editor, headless storefront, browser-operator, localization, media, PWA/offline, frontend-health or web-security work, additionally load `.agents/skills/web-builder-capability-pack/SKILL.md` and map its lanes onto these existing stable specialists/platform experts. When an owner-authorized/public migration, offline reference capture or asset inventory materially benefits from a mirror, additionally load `.agents/skills/site-mirror/SKILL.md`; the mirror engine is a JIT capability, not a new stable identity.
- App/mobile: `@MobileArchitect`, exactly the implementation-stack specialist(s) required (`@FlutterSpecialist` and/or `@ReactNativeSpecialist`), `@MobileQA`, `@AppReleaseEngineer` only when release/build/store delivery is in scope.
- Social: `@SocialStrategy`, `@SocialPublishingOps`, `@SocialAgentOps` when authenticated agent-operated publishing is intended, `@SocialAnalytics`, `@ContentRecycling` when cross-channel reuse is required.
- SEO/AEO/GEO: `@TechnicalSEO`, `@SEOScanner`, platform specialist (`@WordPressSEO`/`@ShopifySEO`) when applicable, `@AEO_GEO` when answer-engine/AI-discovery is material.
- Meta ads: `@MetaAdsEngineer`, `@MetaMeasurement`, `@MarketingScience`, `@IncrementalityAnalyst`, `@AdsCreativeStrategist` according to the actual campaign/measurement question.
- Branding: `@BrandSystemArchitect`, `@BrandBehavior`, `@DesignTokenArchitect`, `@BrandRuntimeEngineer`, independent `@BrandComplianceQA` as material.
- Presentations: load `.agents/skills/presentation-agent-pack/SKILL.md` + `docs/standards/PRESENTATION_ENGINE.md`. Compose the JIT presentation roles (`PresentationResearcher`, `DeckStrategist`, `NarrativeEditor`, `SlideArtDirector`, `AssetCurator`, `DataVizPlanner`, `PPTXEngineer`, `DeckReviewer`) with existing stable owners such as `@Orchestrator`, brand specialists, `@RealAsset`, `@BrandComplianceQA` and `@ProductionQA` according to the deck. Prefer `icip-cas/PPTAgent` for reviewed editable-PPTX workflows, `presenton/presenton` + `presenton/skills` for template/API/multi-format export workflows, and SlideGen-style academic decomposition only when scientific content materially requires it. These engines and presentation roles are JIT capabilities, not new stable identities.

## Procedure
1. Detect project, repository, platform, brand and production constraints.
2. Decompose the task into domain capabilities rather than keywords.
3. Select the smallest sufficient pod; add Upstream Intelligence only for a real tooling/current-source gap or explicit GitHub research.
4. Load the matching domain skill from this expansion; for material web-builder lanes load `web-builder-capability-pack`; load `site-mirror` only for legitimate authorized/public capture work; load `presentation-agent-pack` for PowerPoint/slide/pitch/report/academic presentation work.
5. Route implementation through platform experts where applicable; for presentations preserve source truth, brand rules, editable-output requirements and rendered-slide QA.
6. Preserve authentication/approval boundaries for publishing and ads, access/network/rights boundaries for site mirroring, and license/content-rights boundaries for presentation templates/assets/upstream engines.
7. Require independent QA for material implementation. Presentation builds must render and visually review the final deck; a successful file export is not a QA pass.
8. Report `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT VERIFIED` based on executed evidence, never agent-count theater.

## Output
Selected pod, task boundaries, dependencies, execution evidence, QA outcome and completion state.
