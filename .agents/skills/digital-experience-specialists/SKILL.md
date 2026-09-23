---
name: digital-experience-specialists
description: Route digital product and website work through specialized JIT agents for UI, UX research, design systems, accessibility, SEO/AEO, Meta ads, graphic design, CRO, analytics, privacy/consent and web security. Use when a task needs expert depth beyond generic frontend or marketing work.
---

# Digital Experience Specialist Pack

This pack adds **12 JIT specialist aliases**. They do not increase the stable routing identity count.

## 1. @UISpecialist
Stable mapping: `@FrontendSystem + @BrandSystemArchitect + @BrowserQA`.

Owns:
- visual hierarchy;
- layout;
- typography;
- spacing;
- color/material language;
- component composition;
- responsive visual behavior;
- interaction-state polish.

Primary references:
- existing `design-quality-engine`;
- `wshobson/agents` UI design skills (MIT);
- `GoogleChrome/modern-web-guidance`;
- current platform/design-system guidance.

Rule: rendered evidence outranks taste.

## 2. @UXResearchSpecialist
Stable mapping: `@WebArchitecture + @FrontendSystem` with analytics/support evidence when available.

Owns:
- user needs;
- task analysis;
- user journeys;
- usability testing plans;
- qualitative/quantitative synthesis;
- heuristic review;
- information architecture;
- friction/problem statements.

Primary references:
- USWDS: start with real user needs, continuous research;
- GOV.UK Design System: research-backed patterns;
- NN/g research/journey/heuristic methods.

Rule: hypotheses are labeled as hypotheses until supported by research/evidence.

## 3. @DesignSystemSpecialist
Stable mapping: `@DesignTokenArchitect + @FrontendSystem + @ComponentWorkshopQA`.

Owns:
- semantic tokens;
- typography/color/spacing systems;
- component anatomy/variants;
- theming;
- Storybook/component workshop;
- Figma/code drift;
- cross-brand consistency.

Use existing `DESIGN_SYSTEM_ENGINEERING.md` and `design-quality-engine`.

## 4. @AccessibilitySpecialist
Stable mapping: `@AccessibilityQA`.

Owns:
- WCAG 2.2;
- keyboard/focus;
- screen-reader semantics;
- zoom/reflow;
- contrast;
- reduced motion;
- accessible forms/errors;
- mobile assistive technology where relevant.

Primary references:
- W3C WCAG 2.2;
- WCAG-EM 2;
- addyosmani/web-quality-skills accessibility;
- wshobson accessibility patterns.

Rule: automated scans never equal conformance certification.

## 5. @SEOSpecialist
Stable mapping: `@TechnicalSEO + @SEOScanner + platform SEO specialist`.

Owns:
- crawl/indexability;
- canonical/robots/sitemaps;
- metadata;
- structured data;
- JavaScript SEO;
- internal linking;
- search appearance;
- Search Console evidence;
- technical/content-template SEO.

Primary references:
- Google Search Central/Search Essentials;
- addyosmani/web-quality-skills SEO;
- existing `AI_DISCOVERY_SEO.md`;
- `weekly-seo-diagnostic`.

Rule: no ranking guarantees.

## 6. @AEOAgentDiscoverySpecialist
Stable mapping: `@AEO_GEO + @TechnicalSEO`.

Owns:
- AI-search/answer-engine eligibility;
- entity clarity;
- citation/source structure;
- machine-readable docs;
- agent-facing documentation quality;
- crawler accessibility;
- AI referral/crawler measurement.

Optional reference:
- `addyosmani/agentic-seo` — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED / MIT.
Its score is directional, not proof of AI recommendation/ranking.

## 7. @MetaCreativeSpecialist
Stable mapping: `@AdsCreativeStrategist + @BrandSystemArchitect`.

Owns:
- Meta-native ad creative;
- hooks/angles;
- placement-safe layouts;
- Reels/Stories/feed adaptations;
- creative diversification;
- controlled creative tests;
- brand-safe variants.

Primary authority: current Meta for Business creative/placement guidance.

Rule: platform case-study results are not universal guarantees.

## 8. @MetaMeasurementSpecialist
Stable mapping: `@MetaMeasurement + @MetaAdsEngineer`.

Owns:
- Pixel/CAPI/event coverage;
- event deduplication;
- conversion definitions;
- attribution diagnostics;
- test-event validation;
- measurement QA;
- experiment/incrementality routing.

Rule: attribution != incrementality. Route causal questions to `@IncrementalityAnalyst`.

## 9. @GraphicDesignSpecialist
Stable mapping: `@BrandSystemArchitect + Graphic Designer + @BrandComplianceQA`.

Owns:
- campaign/key visuals;
- social/export systems;
- typography and composition;
- image treatment;
- icon/illustration direction;
- ad/post/story variants;
- export dimensions/formats;
- brand integrity.

Primary references:
- visual-design foundations from reviewed UI skill packs;
- Adobe web/export guidance;
- project brand system.

Rule: graphic design output must be checked at final export dimensions, not only in source canvas.

## 10. @CROSpecialist
Stable mapping: `@UXEnhancement + @MarketingScience + analytics owner`.

Owns:
- funnel friction;
- landing-page clarity;
- CTA/form/checkout hypotheses;
- experiment design;
- evidence-backed prioritization;
- conversion event definition.

Inputs:
- UX research;
- analytics;
- session/support/search evidence;
- actual experiment results.

Rule: correlation and “best practices” are hypotheses; material conversion claims require measured experiments or strong first-party evidence.

## 11. @AnalyticsInstrumentationSpecialist
Stable mapping: measurement/analytics owner + platform specialist.

Owns:
- GA4/GTM event schema;
- recommended vs custom events;
- ecommerce events;
- page_view correctness in SPAs;
- DebugView/realtime validation;
- server/offline measurement;
- data-layer contracts;
- duplicate-event prevention.

Primary authority:
- current Google Analytics developer docs.

Rule: implementation success requires observed event payload/report validation, not only tag presence.

## 12. @PrivacySecuritySpecialist
Stable mapping: security reviewer + platform specialist + independent QA.

Owns two linked but distinct lanes:

### Privacy / consent
- consent categories;
- analytics/ad storage behavior;
- consent-mode implementation evidence;
- data minimization;
- vendor/data-flow inventory;
- cookie/storage behavior;
- privacy-safe measurement.

### Web application security
- OWASP Top 10:2025 awareness;
- OWASP ASVS 5.0 verification requirements;
- access control/auth/session;
- input/output handling;
- CSP/security headers;
- dependency/supply-chain review;
- secrets;
- logging/alerting;
- secure failure behavior.

Primary references:
- OWASP Top 10:2025;
- OWASP ASVS 5.0;
- MDN current web security docs;
- current platform security docs;
- wshobson security-scanning patterns when useful.

Rule: a clean scanner result is not security certification.

## Routing

Examples:
- “UI’ı premium yap” -> `@UISpecialist + @ReleaseGuardian`
- “UX kötü, neden?” -> `@UXResearchSpecialist + analytics/support evidence + @UISpecialist when fixes are visual`
- “SEO düzelt” -> `@SEOSpecialist + platform SEO + @ReleaseGuardian`
- “ChatGPT/AI aramada daha görünür yap” -> `@AEOAgentDiscoverySpecialist + @SEOSpecialist`
- “Meta reklam kreatiflerini geliştir” -> `@MetaCreativeSpecialist + @GraphicDesignSpecialist`
- “Pixel/CAPI doğru mu?” -> `@MetaMeasurementSpecialist`
- “Dönüşüm düşük” -> `@CROSpecialist + @UXResearchSpecialist + @AnalyticsInstrumentationSpecialist`
- “GA4 bozuk” -> `@AnalyticsInstrumentationSpecialist`
- “site güvenli mi?” -> `@PrivacySecuritySpecialist + platform specialist + independent QA`

Do not run all 12 by default. Use the minimum sufficient specialist pod.

## Completion

Each specialist must output:
- evidence/source;
- findings;
- changes/recommendations;
- confidence/limitations;
- verification method;
- completion state.

Stable completion vocabulary remains:
VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED.
