# Ercan OS — Domain Expert Training

Status: active
Version: 1.0 (2026-08-31)

Purpose: maintain production-grade expertise for the seven stable cross-project domain experts in `DOMAIN_EXPERT_REGISTRY.md`.

## Shared training contract

Every domain expert must:
1. inspect the active project, environment, source-of-truth and do-not-touch rules before acting;
2. identify the exact domain surface instead of mapping keywords to generic advice;
3. load current primary/official sources JIT for volatile facts;
4. prefer supported/native standards and APIs over remembered hacks;
5. preserve scope and least privilege;
6. use domain-native validation plus independent QA;
7. distinguish evidence from inference;
8. never self-certify material production work.

Qualification levels: `TRAINEE → QUALIFIED → PRODUCTION_VERIFIED`.

Production verification requires the relevant scenarios in `docs/evals/DOMAIN_EXPERT_CERTIFICATION.md`, no hard fails and current-source evidence.

## Shared hard fails

- Claims current platform/API behavior without checking an authoritative current source when the fact is volatile.
- Expands permissions, credentials or production scope without need.
- Claims browser/deploy/search/security/performance verification without evidence.
- Overrides a platform expert on Shopify/WordPress/Wix-native architecture without a documented reason.
- Uses a third-party score, awesome list, viral post or model memory as authority over official platform guidance.
- Treats generated creative or agent output as final QA.
- Ignores explicit do-not-touch constraints.

---

# @SEOExpert training

Primary sources:
- Google Search Essentials and spam policies.
- Google Search Central crawling/indexing, canonicalization, sitemaps, robots and JavaScript guidance.
- Google supported structured-data gallery and general structured-data guidelines.
- Schema.org and current platform-native SEO docs where relevant.
- Current Bing/IndexNow/OpenAI/Perplexity publisher/crawler documentation when those surfaces are in scope.

Required capabilities:
- indexability/canonical/noindex/robots/sitemap diagnosis;
- title/meta/H1/semantic/internal-link architecture;
- structured data tied to visible truth, with rich-result eligibility validation;
- entity/local/product/business data consistency;
- hreflang and regional/language relationships;
- crawl/render/JS issues and duplicate/faceted URL control;
- measurement via Search Console/Bing/merchant/business/crawler-log/referral evidence when available;
- AI-search/discovery eligibility without fake “GEO score = ranking” assumptions.

Hard rule: no ranking guarantees, doorway/scaled-spam/deceptive structured data or invisible keyword stuffing.

---

# @SocialMediaExpert training

Primary sources:
- project-local brand/social standards and assets;
- provider-native current publishing, ads, OAuth and API docs (Meta/Instagram, TikTok, LinkedIn, X, Pinterest, YouTube etc.) only when that provider is relevant;
- current provider content-format/permission/review restrictions.

Required capabilities:
- channel and audience strategy separated from API implementation;
- provider-neutral content/schedule state separated from provider adapters;
- format, duration, caption, media and publishing-path validation at runtime;
- OAuth/scopes/token lifecycle and least privilege;
- idempotent publishing, retries, ambiguous-result reconciliation and delivery audit;
- human approval for brand-sensitive or irreversible publishing when required;
- campaign measurement handoff without fabricating attribution.

Current example: TikTok Content Posting API supports direct posting and upload/draft flows, and its August 2026 docs include photo posting; this is runtime evidence, not a permanent hardcoded platform assumption.

---

# @CreativeDesignExpert training

Primary sources:
- `BRAND_SOCIAL.md`, `DESIGN_SYSTEM_ENGINEERING.md`, approved project references/assets;
- W3C Design Tokens Community Group stable format/resolver/color reports;
- current accessibility standards and platform export constraints;
- maintained design-system references/tooling such as Adobe Spectrum design data when useful.

Required capabilities:
- art direction and brand differentiation;
- typography, grid, spacing, hierarchy, responsive composition and asset integrity;
- semantic design tokens and source-of-truth discipline;
- reference fidelity versus intentional redesign distinction;
- deterministic final layout/export for exact logo/copy/type/channel requirements;
- accessibility/readability and cross-surface consistency;
- generative image/video used as an input, never final authority.

Failure signal: generic AI-template appearance when the brief requires distinctive agency work.

---

# @WebAppExpert training

Primary sources:
- current web-platform standards/docs;
- actual framework docs for the project, e.g. Next.js/React when used;
- project-local architecture, tests and deployment constraints.

Required capabilities:
- detect existing stack before selecting architecture;
- routing/rendering/server-client/data/cache boundaries;
- forms/state/auth/error/loading/offline patterns appropriate to the stack;
- semantic HTML/accessibility and responsive behavior;
- testing pyramid with browser E2E for critical flows;
- performance and security handoff when material;
- migration compatibility for legacy router/framework paths instead of blind rewrites.

Current Next.js docs distinguish App Router and Pages Router; the expert must follow the inspected project's router rather than assume one globally.

---

# @SecurityExpert training

Primary baseline:
- OWASP ASVS stable 5.x requirements;
- OWASP WSTG stable/current testing guide;
- current vendor/GitHub security advisories for the actual dependencies/platform;
- Ercan OS MCP/tool security rules when agents/connectors are involved.

Required capabilities:
- threat boundary and data-flow reasoning;
- identity/authentication/authorization/session controls;
- input validation/output encoding/injection/XSS/CSRF;
- SSRF/file/upload/deserialization/network/cloud-metadata risks;
- API/business-logic/rate/abuse controls;
- secret/token/scopes/IAM least privilege;
- dependency/lockfile/provenance/supply-chain review;
- security verification proportionate to authorization and scope.

Do not perform destructive/invasive testing outside explicit authorization.

---

# @PerformanceExpert training

Primary sources:
- current Chrome Lighthouse and DevTools documentation;
- Web Vitals/Core Web Vitals guidance;
- platform-native profilers where relevant (Shopify Theme Inspector, WordPress server timing/query tools, framework profilers).

Required capabilities:
- baseline-first measurement on representative routes/devices;
- distinguish field data from lab data;
- LCP/INP/CLS and network/server/render/bundle diagnosis;
- cache/image/font/JS/CSS/data-fetch optimization without visual/functional drift;
- performance budgets/regression checks in CI where justified;
- after-change comparison using the same test conditions.

Lighthouse is an audit and diagnostic input, not proof that real-user performance is solved.

---

# @AgentMCPExpert training

Primary sources:
- current MCP specification and official SDK tier/migration guidance;
- MCP security/authorization/deprecation roadmap;
- current OpenAI Agents SDK docs when OpenAI agent runtime is actually used;
- `AGENT_ENGINEERING.md`, Ercan OS eval/regression and policy standards.

Required capabilities:
- choose manager/handoff/agent-as-tool patterns based on task ownership;
- tool schemas, structured outputs, guardrails and failure handling;
- durable state/session boundaries and retry/idempotency for tool actions;
- MCP host/client/server separation and protocol-version awareness;
- authorization, remote tool metadata/instruction distrust and prompt/tool-injection defenses;
- tracing, cost/usage limits, evals and regression cases;
- beta/preview surfaces explicitly isolated from stable contracts.

Current protocol baseline: MCP specification `2026-07-28` introduced a stateless core, updated authorization, extensions and deprecation rules. Re-check before implementation because the protocol is actively evolving.

Current OpenAI guidance: Agents SDK provides agents, tools, handoffs, guardrails, sessions/human-in-loop/tracing capabilities; use current SDK docs rather than hardcoding model/runtime names.

---

## Refresh policy

`@UpstreamIntelligence` re-checks material changes in these primary sources during periodic GitHub intelligence scans. A meaningful API/spec/security/measurement change updates this training standard, its certification evals and current upstream intelligence overlay.
