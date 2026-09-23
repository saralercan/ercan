---
name: github-specialist-router
description: Route Ercan OS work across reviewed GitHub-backed specialist pods and JIT capability packs for web, app/mobile, social media, YouTube, SEO/AEO/GEO, Meta ads/measurement, branding, presentations, learning/tutoring, platform design, execution governance, founder operations and bounded judgment/decision workflows. Use when the user asks to run all agents for any of these domains, asks to add GitHub experts, or when a material task spans two or more of these domains.
---

# GitHub Specialist Router

Load `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`, root `AGENTS.md`, `docs/standards/AGENT_REGISTRY.md`, and `docs/standards/QUALIFIED_AGENT_ROUTING.md`.

## Routing rule
Treat “tüm ajanları çalıştır” as qualified routing. Select every materially relevant specialist and no unrelated specialist.

## Domain pods
- Web: `@WebArchitecture`, `@FrontendSystem`, `@ScreenshotToCode` when reference-led, `@WebPerformance`, `@AccessibilityQA`, `@BrowserQA`, `@ComponentWorkshopQA` when relevant. For build-from-brief, autonomous/rapid/local builder, visual editor, headless storefront, browser-operator, localization, media, PWA/offline, frontend-health or web-security work, additionally load `.agents/skills/web-builder-capability-pack/SKILL.md` and map its lanes onto these existing stable specialists/platform experts. For screenshot/mockup/Figma/HTML/reference-led WordPress theme reproduction or migration, also load `.agents/skills/wordpress-replica/SKILL.md` + `docs/standards/WORDPRESS_REPLICA_ENGINE.md`; `@WordPressReplica` is a user-facing JIT alias, not a stable identity. When an owner-authorized/public migration, offline reference capture or asset inventory materially benefits from a mirror, additionally load `.agents/skills/site-mirror/SKILL.md`; the mirror engine is a JIT capability, not a new stable identity.
- App/mobile: `@MobileArchitect`, exactly the implementation-stack specialist(s) required (`@FlutterSpecialist` and/or `@ReactNativeSpecialist`), `@MobileQA`, `@AppReleaseEngineer` only when release/build/store delivery is in scope.
- Social: `@SocialStrategy`, `@SocialPublishingOps`, `@SocialAgentOps` when authenticated agent-operated publishing is intended, `@SocialAnalytics`, `@ContentRecycling` when cross-channel reuse is required.
- SEO/AEO/GEO: `@TechnicalSEO`, `@SEOScanner`, platform specialist (`@WordPressSEO`/`@ShopifySEO`) when applicable, `@AEO_GEO` when answer-engine/AI-discovery is material.
- Meta ads: `@MetaAdsEngineer`, `@MetaMeasurement`, `@MarketingScience`, `@IncrementalityAnalyst`, `@AdsCreativeStrategist` according to the actual campaign/measurement question.
- Branding: `@BrandSystemArchitect`, `@BrandBehavior`, `@DesignTokenArchitect`, `@BrandRuntimeEngineer`, independent `@BrandComplianceQA` as material.
- Presentations: load `.agents/skills/presentation-agent-pack/SKILL.md` + `docs/standards/PRESENTATION_ENGINE.md`. Compose the JIT presentation roles (`PresentationResearcher`, `DeckStrategist`, `NarrativeEditor`, `SlideArtDirector`, `AssetCurator`, `DataVizPlanner`, `PPTXEngineer`, `DeckReviewer`) with existing stable owners such as `@Orchestrator`, brand specialists, `@RealAsset`, `@BrandComplianceQA` and `@ProductionQA` according to the deck. Prefer `icip-cas/PPTAgent` for reviewed editable-PPTX workflows, `presenton/presenton` + `presenton/skills` for template/API/multi-format export workflows, and SlideGen-style academic decomposition only when scientific content materially requires it. These engines and presentation roles are JIT capabilities, not new stable identities.

- Learning/tutoring: load `.agents/skills/learning-tutor-engine/SKILL.md` when the user wants step-by-step teaching, codebase onboarding, diagnostics, quizzes or weak-area practice. Route through `@Orchestrator` plus the task-domain specialist; this is JIT, not a stable identity.
- YouTube intelligence: for transcript/search/channel/playlist evidence, optionally load `.agents/skills/youtube-intelligence-provider/SKILL.md` beneath the existing `youtube-growth-engine`. Provider access is read/research only and never implies channel mutation.
- Platform design: load `.agents/skills/platform-design-intelligence/SKILL.md` when Web/Android/Apple platform conventions materially affect the interface. Current official platform guidance outranks community summaries.
- Execution governance: load `.agents/skills/execution-governance/SKILL.md` for bugs, regressions, risky/cross-module edits, repeated failed fixes, fallbacks/adapters or unclear canonical ownership. Keep trivial work on the fast path.
- Founder operations: load `.agents/skills/founder-operations/SKILL.md` for founder strategy, GTM, SOP, PRD, CRO, pricing, outreach or marketing-ops tasks; map to existing business/sales/marketing/product owners rather than creating founder-agent duplicates.
- Judgment engine: load `.agents/skills/judgment-engine/SKILL.md` + `docs/standards/JUDGMENT_ENGINE.md` when code needs a bounded semantic Choice/Noul/Score-style decision, ranking, verification, routing or action selection. TypeSafe/Jev is an optional reviewed provider; deterministic policy/safety/permissions remain authoritative.

## Procedure
1. Detect project, repository, platform, brand and production constraints.
2. Decompose the task into domain capabilities rather than keywords.
3. Select the smallest sufficient pod; add Upstream Intelligence only for a real tooling/current-source gap or explicit GitHub research.
4. Load the matching domain skill from this expansion; for material web-builder lanes load `web-builder-capability-pack`; for reference-led WordPress reconstruction/migration load `wordpress-replica`; load `site-mirror` only for legitimate authorized/public capture work; load `presentation-agent-pack` for PowerPoint/slide/pitch/report/academic presentation work; load the relevant Adaptive Capability Pack skill only when learning, YouTube intelligence, platform design, governed execution or founder operations materially contributes; load `judgment-engine` only when a bounded semantic decision layer materially improves the workflow.
5. Route implementation through platform experts where applicable; for presentations preserve source truth, brand rules, editable-output requirements and rendered-slide QA.
6. Preserve authentication/approval boundaries for publishing and ads, access/network/rights boundaries for site mirroring, and license/content-rights boundaries for presentation templates/assets/upstream engines.
7. Require independent QA for material implementation. Presentation builds must render and visually review the final deck; a successful file export is not a QA pass.
8. Report `VERIFIED`, `PARTIAL`, `BLOCKED`, or `NOT VERIFIED` based on executed evidence, never agent-count theater.

## Output
Selected pod, task boundaries, dependencies, execution evidence, QA outcome and completion state.
