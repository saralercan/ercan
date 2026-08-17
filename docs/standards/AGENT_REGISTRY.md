# Ercan OS Agent Registry

All listed agents inherit root `AGENTS.md`, `AGENT_ENGINEERING.md`, task-relevant domain standards and their project adapter under `projects/`. This registry defines routing focus, not separate constitutions.

## @Orchestrator
Manager/control plane. Owns project routing, JIT context retrieval, task spec compilation, specialist delegation, risk/scope gating, task ledger, synthesis and final completion state. SEO/search/AI-discovery tasks must load `AI_DISCOVERY_SEO.md` and the matching project `SEARCH_VISIBILITY.md` when present. X/Twitter/social-link research loads `SOCIAL_RESEARCH.md` plus `fetch-x-post` and/or `verify-social-claim` JIT skills. Application email/SMTP/API/newsletter/deliverability work loads `MAIL_ENGINEERING.md` plus `mail-platform-selection` and/or `email-delivery-qa` when relevant. Design-token/Figma/component/design-code-drift work loads `DESIGN_SYSTEM_ENGINEERING.md` plus `design-system-bridge` and, when relevant, `accessibility-regression`. Batch deterministic social/brand export may load `creative-export-pipeline`; social publishing automation may load `social-publisher-architecture`. New repo/tool/provider adoption should consult `DISCOVERY_ADOPTION_LEDGER.md` and run `upstream-adoption-audit` for material changes. Repeated agent failures/corrections or new routing/tool behaviors should use `agent-eval-regression`. Google ADK / Agents CLI work loads `GOOGLE_AGENT_PLATFORM.md` only when that provider surface is actually required. Reference-guided generative creative work may load `LUMA_CREATIVE_PROVIDER.md` only when it materially improves the creative task.

## @DragDrop
Adapter: `projects/dragdrop/AGENTS.md`
Manifest: `projects/dragdrop/PROJECT.md`
Search map: `projects/dragdrop/SEARCH_VISIBILITY.md`
Primary domain: Shopify/e-commerce.
Mandatory domain standards: `PLATFORM_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `BRAND_SOCIAL.md` for storefront art direction/social/ads, `DESIGN_SYSTEM_ENGINEERING.md` for shared tokens/components/design-code mapping, `AI_DISCOVERY_SEO.md` for search/entity/product/AI discovery and `MAIL_ENGINEERING.md` only for custom app/B2B/designer mail or notification-template work.
Default QA focus: theme architecture, mobile/mega menu, product/variant, collection, search, cart, checkout handoff, account/localization, Theme Editor, performance, product/feed/entity consistency, shared token/component drift and regression.
Routing note: live storefront is Shopify; do not force WordPress/Hostinger/Google Agent Platform rules onto it unless a separate task explicitly introduces such a service. Shopify-owned transactional notifications remain platform-native unless a custom app/backend workflow genuinely requires another transport. For product lifestyle/editorial creative, Luma is optional only when strict reference-fidelity QA is also enabled.

## @VinterroDigital
Adapter: `projects/vinterro-digital/AGENTS.md`
Manifest: `projects/vinterro-digital/PROJECT.md`
Search map: `projects/vinterro-digital/SEARCH_VISIBILITY.md`
Primary domain: agency/web/brand/social/paid creative.
Hosting/CMS route: Hostinger + WordPress unless a specific surface is verified otherwise.
Mandatory domain standards: `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `DESIGN_SYSTEM_ENGINEERING.md` for design tokens/Figma/code systems and `AI_DISCOVERY_SEO.md` for service/entity/local/search/AI discovery. Load `GOOGLE_AGENT_PLATFORM.md` only for a separate deployable ADK/Google agent-service task. Load `LUMA_CREATIVE_PROVIDER.md` when multi-reference generation/editing or generative video is useful for brand/social/paid creative. Use `creative-export-pipeline` for repeatable post/story/ad/video export systems and `social-publisher-architecture` if an actual publishing backend is being designed.
Default QA focus: brand system, art direction, design tokens, WordPress/site consistency, Instagram feed/Reels/Stories, paid creative, logo/asset integrity, service/entity search visibility, contact/lead/proposal mail reliability, reference fidelity, accessibility and export/channel QA.

## @AyvalıkVibes
Adapter: `projects/ayvalik-vibes/AGENTS.md`
Manifest: `projects/ayvalik-vibes/PROJECT.md`
Search map: `projects/ayvalik-vibes/SEARCH_VISIBILITY.md`
Primary domain: editorial/local guide/social/WordPress.
Hosting/CMS route: Hostinger + WordPress.
Mandatory domain standards: `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAP_ENGINEERING.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `DESIGN_SYSTEM_ENGINEERING.md` for shared UI tokens/components and `AI_DISCOVERY_SEO.md` for editorial/local/search/AI discovery. Google Agent Platform is opt-in only for a distinct agent backend/service. Luma is opt-in only for legitimate creative/editorial generation where real-place/event accuracy is not falsely implied.
Default QA focus: WordPress native architecture, editorial information accuracy/freshness, responsive content, social identity, feed/calendar/event freshness, maps/links, local entity data, partnership/newsletter/form mail reliability, search visibility, design-system consistency and accessibility.

## @GoAyvalık
Adapter: `projects/goayvalik/AGENTS.md`
Manifest: `projects/goayvalik/PROJECT.md`
Search map: `projects/goayvalik/SEARCH_VISIBILITY.md`
Primary domain: local guide/app/web/product experience.
Hosting/CMS route: Hostinger + WordPress unless a specific surface is verified otherwise.
Mandatory domain standards: `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAP_ENGINEERING.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `DESIGN_SYSTEM_ENGINEERING.md` for cross-web/app component/token systems and `AI_DISCOVERY_SEO.md` for structured local/place/search/AI discovery. Load `GOOGLE_AGENT_PLATFORM.md` only if GoAyvalık gains a deployable Google ADK/agent-service surface. Luma is optional for promotional creative, never as a source of truth for maps/places/events.
Default QA focus: product UX, responsive web/app surfaces, localization, maps/content freshness, structured place data, contact/business-listing mail reliability, design-system consistency, brand coherence, search discovery, accessibility and end-to-end critical flows.

## Specialist pool
Orchestrator may instantiate bounded roles such as Shopify Engineer, WordPress Engineer, Hostinger Deployment Engineer, Design System Engineer, Design Token Engineer, Component Workshop/Storybook Engineer, Mail Platform Engineer, Transactional Email Engineer, Email Template Engineer, Deliverability/DNS Reviewer, Email Delivery QA, Browser QA, Visual QA, Accessibility QA, Performance Engineer, SEO Engineer, Entity/Structured Data Specialist, Local SEO Specialist, AI Discovery/GEO Evaluator, Social Research Resolver, Primary-Source Verification Analyst, Upstream Adoption Auditor, Content Strategist, Social Strategist, Instagram Art Director, Graphic Designer, Reels/Video Director, Creative Export Engineer, Social Publisher Architect, Creative Model Provider Specialist, Reference Fidelity Evaluator, Copywriter, Paid Social Strategist, Performance Analyst, Brand QA, Security Reviewer, Agent Platform Engineer, Google ADK/Agents CLI Specialist, Agent Eval/Regression Engineer, Observability Engineer and Strong Advisor.

Specialists receive a delegation contract (objective, boundary, tools/sources, output, success criteria, exclusions) and do not silently expand scope.

## Discovery/adoption routing rule
When research finds a repo/tool/skill/provider, check `DISCOVERY_ADOPTION_LEDGER.md` before creating a new capability. Material adoption uses `upstream-adoption-audit` and ends in `ADOPT`, `ADOPT_PATTERN_ONLY`, `WATCHLIST`, `REJECT` or `SUPERSEDED`. Prefer the smallest integration unit and add regression/eval coverage if agent behavior changes.

## Design-system routing rule
A shared visual foundation or reusable component problem is not solved by changing isolated CSS values on every surface. Route material cross-surface token/Figma/component work through `DESIGN_SYSTEM_ENGINEERING.md` and `design-system-bridge`; pair with `accessibility-regression` where user interaction/semantics are affected.

## Mail routing rule
Human mailbox operations (read/draft/reply/send) route through connected mailbox tools when available; they are not implemented as application SMTP code. Application transactional mail, form notifications, newsletters, provider webhooks, templates and deliverability route through `MAIL_ENGINEERING.md`. Self-hosted mail/MTA infrastructure is a separate architecture decision and is never introduced merely to fix a contact form.

## Social research rule
When the user supplies X/social links, the resolver first establishes exact post identity/body where possible. The verification specialist then evaluates technical/product claims against official docs, verified GitHub repos, release notes or primary research. If exact post content cannot be retrieved, the system must say `POST_BODY_NOT_VERIFIED` rather than infer content from adjacent posts. Social virality, follower count and reposts are not evidence.

## Provider-adapter rule
Provider-specific capabilities are optional adapters, not new constitutions. Google Agents CLI/ADK may be loaded JIT for Google agent-service work; Luma may be loaded JIT for reference-guided image/video generation/editing. Neither may replace the Ercan OS task spec, memory/scope rules, project brand system, independent QA, security boundaries or final completion contract.

A creative provider output is evidence/candidate output, not final approved design. Exact logo/type/layout/product truth and channel requirements remain controlled by `BRAND_SOCIAL.md` + project-local brand assets + independent evaluator.

## Social publishing rule
An internal social publisher must keep provider-neutral scheduling/content state separate from provider-specific API behavior. Official Meta/X/etc. docs and samples are authority; Postiz-class repos are architecture references only. Publishing must be idempotent, retry-aware, token-safe and reconcile ambiguous provider responses.

## Search authority rule
All search/AI-discovery agents prioritize current official platform guidance over third-party GEO scores. Google Search Central, OpenAI crawler/publisher docs, Perplexity crawler docs, Bing/IndexNow docs and Schema.org are authoritative for their respective surfaces. Research/community repos may generate hypotheses and audits but never override platform documentation or justify spam/deceptive tactics.

## Source/hosting rule
Project adapters describe the expected route. Actual live source, hosting account state, Git deployment linkage and platform version must still be inspected at runtime before writes. A project adapter is policy/context, not proof that a deployment is currently connected.

## Future agents
Every new agent inherits the central contract by default. Add it here only when it has a stable routing identity or materially different tool/policy/evaluation contract.
