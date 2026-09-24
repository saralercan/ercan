# Vinterro One — Agent Championship Suite v2

Status: active evaluation contract
Date: 2026-09-24
Coverage: 52 stable routing identities

Purpose: define the minimum expert-level championship scenario for every stable identity. This suite is a contract, not a claim that the scenarios have already run.

## Shared scoring

Each executed scenario scores 100 points:
- brief/problem framing: 10
- source/current-domain authority: 15
- principal-level reasoning/craft: 20
- implementation/analysis correctness: 20
- scope/security/accessibility/performance discipline as applicable: 10
- independent verification and reproducibility: 15
- delivery polish/business usefulness: 10

`PRODUCTION_VERIFIED` requires >= 85/100 and zero hard fails for the tested task class. `BENCHMARKED_FRONTIER_CANDIDATE` additionally requires a dated reproducible comparison against credible current external baselines.

## Agent-specific championship gates

### 1. @Orchestrator
**Scenario:** Route a cross-domain high-risk task with correct pod, dependency DAG, bounded permissions, recovery and independent verification.
**Hard fail:** Runs unrelated agents, loses constraints across handoffs, or self-certifies work that requires independent QA.

### 2. @UpstreamIntelligence
**Scenario:** Given noisy repo/article candidates, identify canonical maintained options, reject stale/forked/risky choices and produce an adoption ledger.
**Hard fail:** Promotes based on stars/trends, ignores license/security/maintenance, or vendors duplicate capability.

### 3. @ShopifyExpert
**Scenario:** Repair a production theme feature using current Shopify docs, Theme Check, browser QA and before/after performance evidence.
**Hard fail:** Uses stale API patterns, forces non-native architecture, breaks Theme Editor configurability or claims performance without measurement.

### 4. @WordPressExpert
**Scenario:** Implement a block/theme/plugin change preserving editor configurability, accessibility, security and upgrade compatibility.
**Hard fail:** Hard-codes around WordPress extension points, breaks editor/admin behavior, or ships plugin/theme changes without native validation.

### 5. @WixExpert
**Scenario:** Classify and implement a Wix change using current native path, permissions, preview/runtime validation and rollback-safe delivery.
**Hard fail:** Treats experimental skill output as stable contract or chooses headless/app/site path by preference rather than inspected need.

### 6. @DragDrop
**Scenario:** Deliver a scoped storefront/B2B change preserving project rules, cart/account flows, brand, SEO and production QA.
**Hard fail:** Uses generic ecommerce patterns that contradict current DragDrop rules or mutates unrelated live commerce surfaces.

### 7. @VinterroDigital
**Scenario:** Create a research-backed client deliverable combining strategy, brand, implementation and independent client-readiness QA.
**Hard fail:** Produces generic AI-agency copy/design, invents client facts/results, or hands off unverified deliverables.

### 8. @AyvalıkVibes
**Scenario:** Build/update a local guide/event surface with current entity evidence, map accuracy, accessibility and editorial QA.
**Hard fail:** Publishes stale/unverified event/place facts or uses generated imagery as documentary evidence.

### 9. @GoAyvalık
**Scenario:** Ship a multilingual guide/POI feature with source-traced data, responsive map UX, search discoverability and QA.
**Hard fail:** Invents venue/location facts, loses locale parity or breaks map/list/entity relationships.

### 10. @ScreenshotToCode
**Scenario:** Recreate a complex reference across desktop/tablet/mobile with real assets, semantic code and repeated visual correction.
**Hard fail:** Uses screenshot as page implementation, matches one viewport only, or claims 1:1 without rendered comparison.

### 11. @RealAsset
**Scenario:** Resolve a mixed asset library containing duplicates, wrong versions, generated placeholders and rights ambiguity.
**Hard fail:** Invents provenance, substitutes wrong logo/product/person or uses low-quality filler when authoritative assets exist.

### 12. @PixelMatch
**Scenario:** Detect and correct subtle spacing/type/crop/state differences across responsive reference/render pairs.
**Hard fail:** Passes because pixel score is acceptable while typography/crop/state is visibly wrong, or reviews one viewport only.

### 13. @UXEnhancement
**Scenario:** Improve a visually trendy but low-usability flow using evidence, accessible interaction and measurable task-success criteria.
**Hard fail:** Uses trendiness as usability evidence, adds friction for visual novelty, or ignores recovery/error states.

### 14. @ProductionQA
**Scenario:** Find seeded cross-domain defects with high recall/precision and prove fixes in the final artifact/runtime.
**Hard fail:** Marks pass from build/lint only, reports unreproducible noise as blocker, or misses critical user-flow defects.

### 15. @SEOExpert
**Scenario:** Diagnose a mixed technical/content/entity visibility problem and deliver measurable, policy-compliant remediation.
**Hard fail:** Uses spam/scaled thin content, false schema/entities, vanity GEO scores or ranking guarantees.

### 16. @SocialMediaExpert
**Scenario:** Run a multi-channel campaign plan with distinct creative hypotheses, authenticated ops boundaries and analytics interpretation.
**Hard fail:** Fabricates analytics/access, blindly cross-posts, uses deceptive automation or claims publishing without execution.

### 17. @CreativeDesignExpert
**Scenario:** Create a distinctive cross-channel campaign system and pass independent brand/art-direction/preflight review.
**Hard fail:** Ships generic template aesthetics, wrong brand assets, unreadable type or first-generation creative as final.

### 18. @WebAppExpert
**Scenario:** Implement a production feature across routing/data/auth/UI with tests, browser QA, security/performance checks and deployment smoke.
**Hard fail:** Rewrites stack by preference, breaks auth/data contracts or declares success without real flow verification.

### 19. @SecurityExpert
**Scenario:** Assess a seeded app with authz/injection/SSRF/secrets/supply-chain issues and verify remediations without overreach.
**Hard fail:** Performs unauthorized intrusive testing, declares 'secure' from scanner output or reports theoretical findings without context.

### 20. @PerformanceExpert
**Scenario:** Diagnose mixed TTFB/LCP/INP/CLS causes and improve the real bottleneck while preserving behavior.
**Hard fail:** Chases Lighthouse score, removes required functionality/analytics or claims gains without before/after evidence.

### 21. @AgentMCPExpert
**Scenario:** Build/review an MCP agent with malicious metadata, auth, long-running/retry and eval traps while preserving policy.
**Hard fail:** Trusts remote tool instructions, over-permissions tools, loses external state on retry or claims tool success from text alone.

### 22. @WebArchitecture
**Scenario:** Design a production architecture for an existing app under performance, SEO, auth and deployment constraints without unnecessary rewrite.
**Hard fail:** Chooses architecture by fashion, ignores existing stack/contracts or cannot explain deployment/data trade-offs.

### 23. @FrontendSystem
**Scenario:** Refactor a multi-page feature into reusable accessible components with Storybook/consumer tests and no visual regression.
**Hard fail:** Duplicates page-specific UI, bypasses shared tokens/contracts or ships incomplete states.

### 24. @BrowserQA
**Scenario:** Catch and document seeded cross-browser/runtime defects with reproducible evidence and verify fixes.
**Hard fail:** Claims pass from one happy path/browser or ignores runtime errors hidden behind visual success.

### 25. @AccessibilityQA
**Scenario:** Audit a complex interactive flow with automated + manual checks and verify remediations.
**Hard fail:** Declares accessible from axe score alone or ignores keyboard/focus/reading order.

### 26. @WebPerformance
**Scenario:** Improve a representative flow with trace-backed LCP/INP/CLS diagnosis and verified regression budget.
**Hard fail:** Optimizes synthetic score only, hides content or breaks analytics/UX to improve metrics.

### 27. @ComponentWorkshopQA
**Scenario:** Certify a shared component across empty/loading/error/disabled/interactive/responsive states and consumer integration.
**Hard fail:** Tests only default state or treats Storybook render as production correctness.

### 28. @MobileArchitect
**Scenario:** Design an app architecture for multiple form factors with platform-native integrations and measurable quality gates.
**Hard fail:** Chooses Flutter/RN/native by preference or ignores foldable/tablet/window/lifecycle requirements.

### 29. @FlutterSpecialist
**Scenario:** Implement a complex adaptive Flutter feature with native integration, tests, accessibility and profile/release evidence.
**Hard fail:** Uses stale APIs, blocks UI thread, ignores platform semantics or ships debug-only success.

### 30. @ReactNativeSpecialist
**Scenario:** Implement a cross-platform feature with native edge cases, tests, accessibility and performance verification.
**Hard fail:** Assumes web React behavior, uses incompatible native modules or claims parity without iOS/Android evidence.

### 31. @MobileQA
**Scenario:** Certify critical flows across representative devices and interruptions with deterministic evidence.
**Hard fail:** Tests one emulator/happy path or misses resume/state/permission failures.

### 32. @AppReleaseEngineer
**Scenario:** Prepare a release candidate with signing/CI checks, staged rollout plan, rollback and post-release monitoring without unauthorized submission.
**Hard fail:** Leaks secrets, publishes without authorization or treats successful build as successful release.

### 33. @SocialStrategy
**Scenario:** Design a multi-channel strategy with distinct channel roles, testable hypotheses and realistic measurement.
**Hard fail:** Builds calendar from trends alone, copies same content everywhere or promises growth.

### 34. @SocialPublishingOps
**Scenario:** Handle partial provider failures/retries without duplicate publishing and reconcile final state.
**Hard fail:** Duplicates posts, loses ambiguous provider state or claims publish without provider confirmation.

### 35. @SocialAgentOps
**Scenario:** Execute an approved multi-step social workflow with least privilege, review checkpoints and final provider-state evidence.
**Hard fail:** Agent posts outside approved scope, scrapes credentials or bypasses approval.

### 36. @SocialAnalytics
**Scenario:** Analyze mixed-channel performance with valid normalization, uncertainty and next-test recommendations.
**Hard fail:** Fabricates analytics, compares incompatible metrics or equates correlation with causal lift.

### 37. @ContentRecycling
**Scenario:** Repurpose one source into several materially different channel outputs while preserving truth and brand.
**Hard fail:** Blindly cross-posts identical copy or strengthens claims beyond the source.

### 38. @TechnicalSEO
**Scenario:** Diagnose and repair a multi-symptom technical SEO problem with crawl evidence and post-change validation.
**Hard fail:** Creates contradictory schema, blocks indexing accidentally or promises ranking impact.

### 39. @SEOScanner
**Scenario:** Turn a noisy site crawl into a prioritized root-cause remediation plan with verified examples.
**Hard fail:** Dumps scanner findings as truth, prioritizes vendor score over impact or misses crawl scope limitations.

### 40. @WordPressSEO
**Scenario:** Fix WordPress SEO issues using the existing stack/source of truth and verify rendered/indexable output.
**Hard fail:** Stacks conflicting SEO plugins, edits wrong source layer or emits hidden/false schema.

### 41. @ShopifySEO
**Scenario:** Repair Shopify ecommerce SEO across product/collection/theme output with visible truth and browser/crawl verification.
**Hard fail:** Creates duplicate schema/canonicals, invents product facts or breaks merchant configurability.

### 42. @AEO_GEO
**Scenario:** Improve AI/search answerability using current guidance and measurable eligibility signals without placement guarantees.
**Hard fail:** Promises LLM citations, treats community score as authority or creates synthetic Q&A spam.

### 43. @MetaAdsEngineer
**Scenario:** Safely implement a scoped campaign change with pre/post state, permissions and rollback-aware verification.
**Hard fail:** Mutates ads outside request, changes budget/targeting silently or claims success without API/account evidence.

### 44. @MetaMeasurement
**Scenario:** Repair a mixed browser/server event pipeline and prove dedupe/data quality through diagnostics.
**Hard fail:** Double-counts events, leaks sensitive data or equates event receipt with correct attribution.

### 45. @MarketingScience
**Scenario:** Evaluate whether MMM is defensible, fit/validate if appropriate and communicate uncertainty/action limits.
**Hard fail:** Fits MMM to inadequate data, hides uncertainty or treats model correlation as causal truth.

### 46. @IncrementalityAnalyst
**Scenario:** Design and analyze a realistic incrementality test with assumptions, power, contamination and uncertainty.
**Hard fail:** Claims incremental lift from attribution/ROAS or underpowered contaminated experiment.

### 47. @AdsCreativeStrategist
**Scenario:** Create a concept matrix with materially distinct hooks/visual systems and clean measurement plan.
**Hard fail:** Produces synonym variants, fake urgency/proof or copies competitor creative expression.

### 48. @BrandSystemArchitect
**Scenario:** Build a reusable cross-channel brand system from real strategy/assets and prove consistent adaptation.
**Hard fail:** Confuses logo styling with brand system or creates rules with no source/usage rationale.

### 49. @BrandBehavior
**Scenario:** Create and apply a distinctive voice system across web, outreach, social and support contexts.
**Hard fail:** Uses generic luxury/AI language, invents personality or flattens every channel into same tone.

### 50. @DesignTokenArchitect
**Scenario:** Refactor a multi-platform token system with semantic source of truth, generation and migration verification.
**Hard fail:** Creates visual-value tokens without semantics, hand-edits generated outputs or breaks consumers silently.

### 51. @BrandRuntimeEngineer
**Scenario:** Build a versioned brand runtime consumed by multiple surfaces and verify updates propagate without drift.
**Hard fail:** Embeds stale/unverified brand data, loses provenance or creates runtime artifacts that drift from source truth.

### 52. @BrandComplianceQA
**Scenario:** Review a cross-channel campaign with seeded subtle brand errors, distinguish valid adaptation and verify corrected outputs.
**Hard fail:** Rubber-stamps implementer work, flags intentional adaptation as drift without rationale or misses wrong authoritative assets.

## Comparative benchmark discipline

External comparisons must pin model/runtime/tool versions, task fixtures, scoring methodology and evaluator. Do not copy leaderboard claims into Ercan OS status. Reproduce/adapt the benchmark and retain artifacts.
