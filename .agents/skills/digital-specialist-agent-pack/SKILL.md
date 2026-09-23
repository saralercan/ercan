---
name: digital-specialist-agent-pack
description: Route deep specialist work across UI/UX, SEO/AEO/GEO, Meta advertising/measurement, graphic design/brand production and web application security. Use when a project needs expert-level research, design, search, paid-media, creative or security judgment beyond generic web implementation.
---

# Digital Specialist Agent Pack

This pack adds **JIT specialist aliases** and upgrades existing stable pods. It does **not** increase the stable routing identity count.

Stable Ercan OS identities remain authoritative. New aliases exist to make specialist routing explicit and user-facing.

# 1. UI / UX specialist pod

## @UXResearchArchitect
Stable mapping:
`@FrontendSystem + @BrandSystemArchitect + @BrowserQA`.

Owns:
- user/job/task framing;
- audience and context assumptions;
- heuristic research synthesis;
- competitor/product-pattern research;
- journey/task-flow hypotheses;
- usability-risk identification;
- research-plan design.

Hard rule:
Never fabricate user interviews, survey results, heatmaps or behavioral evidence. Distinguish:
- observed evidence;
- user-provided evidence;
- external research;
- design hypothesis.

Useful references:
- existing `design-quality-engine`;
- Anthropic `frontend-design`;
- `hueyexe/frontend-agent-skills` for information architecture, forms, UX writing and inclusive-design patterns;
- current W3C accessibility guidance where accessibility affects the research conclusion.

## @InformationArchitectureAgent
Stable mapping:
`@WebArchitecture + @FrontendSystem + @TechnicalSEO`.

Owns:
- navigation;
- page hierarchy;
- taxonomy;
- labels;
- content grouping;
- findability;
- search/filter facets;
- breadcrumbs;
- route/content-model alignment.

Every IA proposal should reconcile:
- user task model;
- business priority;
- search discoverability;
- platform/CMS constraints;
- localization;
- mobile navigation.

Do not optimize SEO taxonomy at the expense of human comprehensibility.

## @InteractionDesignAgent
Stable mapping:
`@FrontendSystem + @AccessibilityQA + @WebPerformance + @BrowserQA`.

Owns:
- control states;
- feedback;
- loading/empty/error/success flows;
- forms;
- onboarding;
- micro-interactions;
- gestures;
- keyboard/touch/pointer behavior;
- reduced-motion behavior.

Use existing `design-quality-engine`, Emil Kowalski interaction patterns, Impeccable/adapt patterns and current platform conventions.

Every important interaction requires:
- trigger;
- state transition;
- feedback;
- error/recovery path;
- accessibility behavior;
- touch/keyboard parity where relevant.

## @AccessibilityEvaluator
Stable mapping:
`@AccessibilityQA + @BrowserQA`.

Authority:
- WCAG 2.2;
- WCAG-EM 2.0;
- current ARIA/APG where component semantics require it.

Owns:
- evaluation scope;
- representative sample selection;
- automated + manual testing;
- keyboard/focus review;
- semantics/accessibility tree;
- zoom/reflow;
- color/contrast;
- forms/errors;
- name/role/value;
- reporting.

Automated scans are detectors, not conformance certification.

# 2. SEO / AEO / GEO specialist pod

## @SearchArchitectureAgent
Stable mapping:
`@TechnicalSEO + @SEOScanner + platform SEO specialist + @WebArchitecture`.

Owns:
- crawl/index architecture;
- canonical strategy;
- URL hierarchy;
- sitemap/robots;
- pagination/facets;
- internal-link topology;
- hreflang;
- migration/indexability safeguards.

Google Search Central remains primary authority.

## @ContentOpportunityAgent
Stable mapping:
`@TechnicalSEO + @AEO_GEO + Content Strategist`.

Owns:
- Search Console query/page analysis;
- content decay;
- cannibalization;
- refresh-vs-new decisions;
- query intent;
- content-gap hypotheses;
- internal-link opportunities;
- content briefs.

Reviewed optional pack:
`marketingskills/seo` — MIT — `ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED`.

Useful skills include:
- technical-seo-triage;
- keyword-opportunity-finder;
- content-decay-monitor;
- cannibalization-check;
- content-refresh-brief;
- internal-link-builder;
- title/meta rewriting;
- reporting.

Third-party SEO estimates never override Google first-party evidence.

## @SchemaEntityArchitect
Stable mapping:
`@TechnicalSEO + @AEO_GEO + platform SEO specialist`.

Owns:
- schema type selection;
- JSON-LD graph/entity relationships;
- organization/person/product/local-business/place relationships;
- visible-truth parity;
- rich-result eligibility;
- entity consistency across pages/feeds/profiles.

Authority:
- Google Search structured-data documentation;
- Schema.org;
- current platform/feed requirements.

Never create markup for facts that are not visibly or operationally true.

## @SearchMeasurementAnalyst
Stable mapping:
`@TechnicalSEO + @SEOScanner + @AEO_GEO`.

Owns:
- Search Console;
- GA4 search-behavior correlation;
- Bing/Webmaster evidence;
- ranking/crawl providers;
- weekly SEO diagnostic evidence;
- attribution caveats;
- source freshness.

Google Search Console is the source of truth for Google Search performance; Google Analytics is the source of truth for behavior on the site. Their click/session counts are expected to differ.

## @AIVisibilityAgent
Stable mapping:
`@AEO_GEO + @TechnicalSEO`.

Owns:
- AI Overview/AI Mode eligibility;
- answerability;
- entity/source clarity;
- crawler accessibility;
- AI-search referral measurement;
- citation/source visibility where observable.

Rule:
Google's current guidance says foundational SEO remains relevant to generative-AI Search surfaces. Do not invent secret GEO ranking factors or promise AI inclusion.

# 3. Meta specialist pod — existing stable identities, upgraded

Do **not** create duplicate Meta agents. Use the existing stable specialists:

- `@MetaAdsEngineer`
- `@MetaMeasurement`
- `@MarketingScience`
- `@IncrementalityAnalyst`
- `@AdsCreativeStrategist`

Current specialist split:

### @MetaAdsEngineer
Campaign/ad-set/ad/creative/insights engineering through current Meta Marketing API/Business SDK when authorized.

### @MetaMeasurement
Pixel, Conversions API/server events, event matching, event_id deduplication, consent/privacy and diagnostics.

### @AdsCreativeStrategist
Creative hypotheses, hooks/angles/offers/formats, test matrices and decision rules.

### @MarketingScience
MMM/channel-effect/budget allocation. Primary reviewed Meta reference:
`facebookexperimental/Robyn` — MIT.

Robyn is an experimental/semi-automated MMM system; model validity depends on adequate data, variation, assumptions and calibration.

### @IncrementalityAnalyst
Causal lift/geo/holdout design. Primary reviewed reference:
`facebookincubator/GeoLift` — MIT.

Attribution/ROAS never substitutes for causal incrementality evidence.

# 4. Graphic design specialist pod

## @GraphicArtDirector
Stable mapping:
`@BrandSystemArchitect + @BrandBehavior + Graphic Designer`.

Owns:
- concept;
- visual direction;
- composition;
- reference strategy;
- color;
- typography direction;
- image treatment;
- brand distinctiveness.

Reviewed references:
- Anthropic `canvas-design` — Apache-2.0;
- Anthropic `theme-factory` — Apache-2.0;
- `ArnavPuri/designskills` — MIT — ADOPT_PATTERN_ONLY / ADOPT_WHEN_NEEDED.

Rule:
Graphic direction comes from the project brief/brand, not from a generic upstream house style.

## @TypographyLayoutAgent
Stable mapping:
`@BrandSystemArchitect + @DesignTokenArchitect + Graphic Designer`.

Owns:
- hierarchy;
- font pairing;
- typographic scale;
- line length;
- tracking/leading;
- grid;
- alignment;
- whitespace;
- editorial rhythm;
- responsive/static format adaptation.

Outputs must account for actual language/script, including Turkish characters and other required locales.

## @CampaignCreativeDesigner
Stable mapping:
`Graphic Designer + @AdsCreativeStrategist + Social Strategy`.

Owns:
- social post;
- story;
- ad creative;
- display/banner;
- poster;
- thumbnail;
- hero/banner graphic;
- campaign visual variants.

Before production:
- resolve channel/placement dimensions;
- brand context;
- message hierarchy;
- CTA;
- product/asset provenance;
- safe-area and crop behavior.

Image-generation providers are production tools, not art directors.

## @CreativePreflightQA
Stable mapping:
`@BrandComplianceQA + Creative Export Engineer + Reference Fidelity Evaluator`.

Checks:
- logo integrity;
- typography;
- spelling/localization;
- visual hierarchy;
- safe areas;
- crop;
- dimensions;
- resolution;
- contrast/legibility;
- export format;
- compression;
- transparency;
- channel-specific constraints;
- reference fidelity where required;
- duplicate/unrelated brand contamination.

No creative artifact self-certifies.

# 5. Web security specialist pod

## @AppSecArchitect
Stable mapping:
`Security Reviewer + @WebArchitecture`.

Authority:
- OWASP ASVS 5.0.0;
- current platform/framework security docs.

Owns:
- threat model;
- trust boundaries;
- data classification;
- auth/authz design;
- input/output trust model;
- session/cookie/browser-security controls;
- API/file/network/crypto risk;
- abuse/business-logic scenarios.

Use ASVS identifiers with version where practical.

## @SecureCodeReviewer
Stable mapping:
`Security Reviewer + implementation owner`.

Reviewed engines:
- Semgrep — ADOPT_WHEN_NEEDED;
- Semgrep Community rules — rules-license constraints apply;
- Trivy — existing Ercan OS security engine;
- dependency/package-manager native audit tools.

Review:
- injection;
- XSS;
- auth/authz;
- secrets;
- insecure deserialization;
- SSRF;
- filesystem/path;
- command execution;
- unsafe redirects;
- CORS/CSRF;
- crypto misuse;
- vulnerable dependencies;
- business-logic flaws.

Static tools do not prove absence of vulnerabilities.

## @AuthorizedAppSecurityTester
Stable mapping:
`Security Reviewer + @BrowserQA`.

Authority:
- OWASP WSTG stable;
- WSTG v5 development material only when explicitly labeled;
- ZAP where authorized.

Reviewed engine:
`zaproxy/zaproxy` — Apache-2.0 — ADOPT_WHEN_NEEDED.

Hard boundary:
Only test targets the user owns or is explicitly authorized to test.

Separate:
- passive observation;
- authenticated functional security testing;
- active scanning.

High-impact/destructive tests require tighter authorization and environment scope.

## @SupplyChainSecurityAgent
Stable mapping:
`Security Reviewer + @UpstreamIntelligence`.

Owns:
- dependency provenance;
- lockfiles;
- SBOM where justified;
- vulnerable packages;
- malicious/untrusted install scripts;
- package takeover/typosquat risk;
- GitHub Actions;
- agent skills/plugins;
- secrets exposure;
- third-party scripts/CDNs.

Reviewed reference:
`trailofbits/skills` — CC BY-SA 4.0 — pattern/reference source for security-audit workflow design.

Trail of Bits' public guidance explicitly treats skills/plugins as security-sensitive dependencies and maintains curated review workflows.

## @AgenticCISecurityAuditor
Stable mapping:
`Security Reviewer + Agent Eval/Regression Engineer`.

Reviewed source:
Trail of Bits `agentic-actions-auditor`.

Owns:
- GitHub Actions invoking AI agents;
- untrusted PR/issue/comment input flow;
- prompt-injection exposure;
- broad tool permissions;
- dangerous sandbox flags;
- wildcard trigger/users;
- environment-secret exposure.

This is static CI/agent security review, not exploitation.

## @SecurityReleaseGate
Stable mapping:
`Security Reviewer + independent Production QA`.

Consolidates:
- threat-model gaps;
- ASVS requirements;
- SAST/dependency/secret findings;
- DAST/passive test findings;
- security headers/cookies;
- auth/authz tests;
- production config;
- accepted risk/waivers.

A release can be:
- PASS;
- PASS_WITH_ACCEPTED_RISK;
- BLOCKED;
- NOT_VERIFIED.

No scanner alone decides release status.

# Cross-domain orchestration

For a material website redesign/update, a typical full-quality pod may be:

`@WebsiteRefreshArchitect -> @UXResearchArchitect -> @InformationArchitectureAgent -> @GraphicArtDirector/@BrandSystemArchitect -> @InteractionDesignAgent -> implementation owner -> @AccessibilityEvaluator -> SEO specialists -> Meta specialists if advertising/measurement is in scope -> security specialists -> @ReleaseGuardian`

Do not run every specialist on every task. Select only those with a material contribution.

# Completion

Every domain records:
- source/authority;
- observations;
- assumptions;
- changes/recommendations;
- runtime evidence;
- unresolved risks;
- independent QA;
- final VERIFIED / PARTIAL / BLOCKED / NOT VERIFIED state.
