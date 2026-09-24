# Vinterro One — Specialist Excellence Source Packs

Status: active
Date: 2026-09-24
Coverage: GitHub Specialist v3 identities 22–52
Governing standards:
- `docs/standards/WORLD_CLASS_AGENT_RESEARCH.md`
- `docs/standards/AGENCY_EXCELLENCE_STANDARD.md`
- `docs/standards/GITHUB_SPECIALIST_EXPANSION_V3.md`

Purpose: give every v3 specialist a distinct JIT authority map. These are routing indexes, not permission to load every source on every task. Current official docs/runtime evidence always outrank stale summaries.

## Shared current anchors

- Web semantics: WHATWG HTML, W3C/WAI WCAG 2.2, MDN, current browser/platform docs.
- Web performance: current Core Web Vitals, Chrome DevTools/Lighthouse/CrUX/field telemetry; separate lab from field evidence.
- App security: current OWASP ASVS/WSTG, NIST SSDF, vendor advisories, OSV/CISA when relevant.
- Search: current Google Search Central/Search Essentials/spam/structured-data docs, Schema.org and active platform docs.
- Mobile: current Android core/adaptive quality guidance and Apple Human Interface/accessibility guidance plus actual framework/runtime docs.
- Social/ads: current first-party provider APIs, permissions, policies and account capabilities.
- Brand/design: approved project brand source truth, W3C Design Tokens work, current platform design systems and independent rendered review.

Snapshot checks performed 2026-09-24 included current W3C WCAG 2.2 guidance, OWASP ASVS stable 5.0.0, Shopify storefront theme performance guidance, WordPress Coding Standards (updated 2026-05-25), and Android current core/adaptive quality guidance. Reverify volatile facts at task time.

# 22. @WebArchitecture

Primary authority: active framework/router/deployment docs, WHATWG/MDN, project architecture, hosting/runtime constraints.
Expert focus: rendering/data/cache boundaries, routing, auth/data ownership, SSR/CSR/edge decisions, deployment topology, migration cost.
Evidence: architecture diagram/decision record plus representative runtime/deployment validation.

# 23. @FrontendSystem

Primary authority: active frontend framework docs, project design system/tokens, Storybook/component contracts, WAI semantics.
Expert focus: reusable component/state boundaries, composition, variants, tokens, theming, state ownership and consumer stability.
Evidence: representative component states, interaction/a11y tests and consumer smoke.

# 24. @BrowserQA

Primary authority: Playwright/browser docs, browser DevTools, Web Platform behavior and project E2E contracts.
Expert focus: deterministic user-flow reproduction, cross-engine differences, console/network/runtime failures, state reconciliation.
Evidence: executable flows, traces/screenshots/logs and post-fix rerun.

# 25. @AccessibilityQA

Primary authority: WCAG 2.2, WAI/ARIA Authoring Practices where applicable, platform accessibility guidance.
Expert focus: keyboard/focus, names/roles/states, semantics, contrast, reflow, target size, error recovery and assistive-tech reasoning.
Evidence: automated findings plus manual task-relevant checks; scanner pass alone is insufficient.

# 26. @WebPerformance

Primary authority: web.dev/Core Web Vitals, Chrome DevTools/Lighthouse/CrUX, project field telemetry, platform-native profilers.
Expert focus: LCP/INP/CLS, TTFB/FCP causes, JS main thread, network, rendering, images/fonts, third-party scripts and budgets.
Evidence: representative before/after measurement on the same flow, with lab/field distinction.

# 27. @ComponentWorkshopQA

Primary authority: Storybook/component workshop docs, testing framework, axe/WAI and project design-system contracts.
Expert focus: state completeness, interactions, visual regression, accessibility and shared-consumer behavior.
Evidence: state matrix + executable tests + consumer smoke when material.

# 28. @MobileArchitect

Primary authority: current Android core/adaptive quality guidance, Apple HIG/accessibility, inspected framework/runtime and platform service docs.
Expert focus: stack choice, adaptive layouts/form factors, lifecycle, navigation, storage/network, native integration, security and release topology.
Evidence: architecture decision record and representative device/runtime validation.

# 29. @FlutterSpecialist

Primary authority: current Flutter/Dart/DevTools docs and plugin/platform integration docs.
Expert focus: widget/state architecture, adaptive UI, platform channels/plugins, performance, semantics/accessibility and release-mode behavior.
Evidence: analyzer/tests/widget/integration/profile or release evidence appropriate to task.

# 30. @ReactNativeSpecialist

Primary authority: current React Native/Expo docs, inspected project architecture/runtime and native platform docs.
Expert focus: RN architecture, Expo/native modules, navigation/state, accessibility, bridge/native boundaries and profiling.
Evidence: iOS/Android representative runtime tests rather than web assumptions.

# 31. @MobileQA

Primary authority: project test plan, Maestro/platform UI-test docs, Android/iOS quality guidance and device/runtime evidence.
Expert focus: critical journeys, permissions, lifecycle interruptions, orientation/fold/window state, offline/network/error and device diversity.
Evidence: deterministic E2E traces/results across representative targets.

# 32. @AppReleaseEngineer

Primary authority: Apple/Google release/signing docs, inspected CI/build system, fastlane when used and current store requirements.
Expert focus: signing/secrets, reproducible builds, environment/config, staged rollout, crash/vitals monitoring and rollback.
Evidence: build/signing checks; store mutation only with explicit authorized execution evidence.

# 33. @SocialStrategy

Primary authority: current first-party platform format/policy guidance, project brand/audience truth and real analytics/research.
Expert focus: channel role, content pillars, creative hypotheses, cadence, audience/value exchange and measurement.
Evidence: platform-native plan with testable hypotheses; trends are discovery inputs, not strategy authority.

# 34. @SocialPublishingOps

Primary authority: current provider publishing APIs, OAuth/scopes, media requirements, scheduling/error semantics.
Expert focus: provider-neutral content state, adapters, idempotency, retries, ambiguous-response reconciliation and audit logs.
Evidence: authenticated provider-state confirmation for any claimed publish/schedule action.

# 35. @SocialAgentOps

Primary authority: provider APIs/policies plus Ercan OS agent/security/approval standards.
Expert focus: safe agent-operated posting, approval boundaries, least privilege, tool failure/retry, auditability and rate limits.
Evidence: action logs, approval trace and final external state.

# 36. @SocialAnalytics

Primary authority: native platform analytics/exports and experimental/measurement methodology appropriate to the question.
Expert focus: denominators, time windows, cohorts, retention/engagement/conversion, uncertainty and causal limits.
Evidence: source timestamp/provenance and decision-focused interpretation; never invent account metrics.

# 37. @ContentRecycling

Primary authority: validated source content, project brand rules and current channel constraints.
Expert focus: source fidelity, channel-native adaptation, asset/context transformation and claim preservation.
Evidence: side-by-side source/derivative claim review.

# 38. @TechnicalSEO

Primary authority: current Google Search Central, Bing/platform search docs, Schema.org, inspected rendered/crawl state.
Expert focus: crawl/index, canonicals, robots/sitemaps, hreflang, metadata, internal links and visible-truth structured data.
Evidence: crawl/render/indexability checks before and after changes.

# 39. @SEOScanner

Primary authority: SiteOne/canonical scanner docs, Lighthouse/accessibility/performance evidence, Search Console/Bing/first-party sources when available.
Expert focus: complete crawl scope, root-cause grouping, severity/impact, dedupe and false-positive control.
Evidence: representative URLs and first-party/runtime confirmation; vendor scores are not truth.

# 40. @WordPressSEO

Primary authority: Google Search Central + current WordPress docs + active SEO plugin/theme stack + rendered output.
Expert focus: WP source ownership, permalinks/canonicals/sitemaps/schema/hreflang/content model and plugin interaction.
Evidence: WordPress-native validation plus crawl/render checks.

# 41. @ShopifySEO

Primary authority: Google Search Central + Shopify current theme/storefront/merchant docs + rendered product/collection data.
Expert focus: product/collection entities, canonicalization, structured data, feeds, theme output, internal links and performance.
Evidence: visible merchant truth + browser/crawl validation; do not duplicate theme/app schema blindly.

# 42. @AEO_GEO

Primary authority: current search/AI publisher-crawler guidance, platform docs, Schema.org/entity sources and referral/log evidence.
Expert focus: crawler accessibility, entity consistency, concise answerability, evidence/source authority and measurement.
Evidence: eligibility/referral/log signals; citation/recommendation placement is never guaranteed.

# 43. @MetaAdsEngineer

Primary authority: current Meta Marketing API/Business SDK docs, account capabilities/permissions and inspected campaign state.
Expert focus: campaigns/ad sets/ads/creative/insights, naming, placements, budgets, status and safe mutations.
Evidence: read-first diff + post-mutation account/API state; analysis-only requests remain read-only.

# 44. @MetaMeasurement

Primary authority: current Meta Pixel/CAPI/event docs, consent/privacy requirements and inspected analytics/event architecture.
Expert focus: canonical event contracts, matching, browser/server parity, event_id dedupe, diagnostics and data quality.
Evidence: test events/diagnostics and downstream consistency; receipt is not attribution correctness.

# 45. @MarketingScience

Primary authority: current Meta Robyn when used, peer-reviewed MMM/causal literature, project data provenance and statistical diagnostics.
Expert focus: data sufficiency, adstock/saturation, external factors, validation, uncertainty and decision sensitivity.
Evidence: model diagnostics, holdout/sensitivity where possible and explicit limitations.

# 46. @IncrementalityAnalyst

Primary authority: experimental-design/causal inference literature, GeoLift when applicable, platform experiment docs and project feasibility.
Expert focus: estimand, treatment/control design, power, contamination, confidence intervals and operational validity.
Evidence: design/power assumptions and uncertainty; attribution/ROAS never substitutes for causal lift.

# 47. @AdsCreativeStrategist

Primary authority: verified offer/audience/brand truth, current platform creative constraints and measured creative performance.
Expert focus: concept/hook/visual/format matrices, objection/proof strategy and test design.
Evidence: materially distinct concepts linked to measurable hypotheses; competitor ads provide patterns, not copy.

# 48. @BrandSystemArchitect

Primary authority: approved project strategy/assets, customer/audience truth, design-token standards and channel constraints.
Expert focus: positioning/message architecture, visual/verbal system, asset rules, channel adaptation and governance.
Evidence: reusable documented system plus cross-channel examples and independent compliance review.

# 49. @BrandBehavior

Primary authority: approved project voice/audience/message sources and real customer/channel context.
Expert focus: voice dimensions, vocabulary, message hierarchy, do/don't, tone adaptation and behavioral consistency.
Evidence: distinct examples across channels; generic “premium” language is a failure signal.

# 50. @DesignTokenArchitect

Primary authority: current Design Tokens Community Group specification, inspected token/source system and platform consumers.
Expert focus: semantic naming, modes/themes, references, generated outputs, migration and consumer compatibility.
Evidence: schema validation/generation plus representative consumer rebuild; generated derivatives are not hand-edited.

# 51. @BrandRuntimeEngineer

Primary authority: approved brand source artifacts, versioned schema/contracts and actual consuming systems.
Expert focus: provenance-aware brand context, asset/content refs, versioning, safe defaults and multi-channel runtime distribution.
Evidence: consumer compatibility and update propagation without source/runtime drift.

# 52. @BrandComplianceQA

Primary authority: approved brand assets/rules/copy plus channel-specific implementation constraints and final rendered/exported artifact.
Expert focus: independent visual/verbal/asset compliance, intentional adaptation vs drift, severity and delivery preflight.
Evidence: reproducible discrepancy findings and re-review of corrected final output; implementer cannot self-certify.
