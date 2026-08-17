# Ercan OS Agent Registry

All listed agents inherit root `AGENTS.md`, `AGENT_ENGINEERING.md`, task-relevant domain standards and their project adapter under `projects/`. This registry defines routing focus, not separate constitutions.

## @Orchestrator
Manager/control plane. Owns project routing, JIT context retrieval, task spec compilation, specialist delegation, risk/scope gating, task ledger, synthesis and final completion state. SEO/search/AI-discovery tasks must load `AI_DISCOVERY_SEO.md` and the matching project `SEARCH_VISIBILITY.md` when present. Google ADK / Agents CLI work loads `GOOGLE_AGENT_PLATFORM.md` only when that provider surface is actually required. Reference-guided generative creative work may load `LUMA_CREATIVE_PROVIDER.md` only when it materially improves the creative task.

## @DragDrop
Adapter: `projects/dragdrop/AGENTS.md`
Manifest: `projects/dragdrop/PROJECT.md`
Search map: `projects/dragdrop/SEARCH_VISIBILITY.md`
Primary domain: Shopify/e-commerce.
Mandatory domain standards: `PLATFORM_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `BRAND_SOCIAL.md` for storefront art direction/social/ads and `AI_DISCOVERY_SEO.md` for search/entity/product/AI discovery.
Default QA focus: theme architecture, mobile/mega menu, product/variant, collection, search, cart, checkout handoff, account/localization, Theme Editor, performance, product/feed/entity consistency and regression.
Routing note: live storefront is Shopify; do not force WordPress/Hostinger/Google Agent Platform rules onto it unless a separate task explicitly introduces such a service. For product lifestyle/editorial creative, Luma is optional only when strict reference-fidelity QA is also enabled.

## @VinterroDigital
Adapter: `projects/vinterro-digital/AGENTS.md`
Manifest: `projects/vinterro-digital/PROJECT.md`
Search map: `projects/vinterro-digital/SEARCH_VISIBILITY.md`
Primary domain: agency/web/brand/social/paid creative.
Hosting/CMS route: Hostinger + WordPress unless a specific surface is verified otherwise.
Mandatory domain standards: `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `UPSTREAM_TOOLCHAIN.md`; add `AI_DISCOVERY_SEO.md` for service/entity/local/search/AI discovery. Load `GOOGLE_AGENT_PLATFORM.md` only for a separate deployable ADK/Google agent-service task. Load `LUMA_CREATIVE_PROVIDER.md` when multi-reference generation/editing or generative video is useful for brand/social/paid creative.
Default QA focus: brand system, art direction, design tokens, WordPress/site consistency, Instagram feed/Reels/Stories, paid creative, logo/asset integrity, service/entity search visibility, reference fidelity and export/channel QA.

## @AyvalıkVibes
Adapter: `projects/ayvalik-vibes/AGENTS.md`
Manifest: `projects/ayvalik-vibes/PROJECT.md`
Search map: `projects/ayvalik-vibes/SEARCH_VISIBILITY.md`
Primary domain: editorial/local guide/social/WordPress.
Hosting/CMS route: Hostinger + WordPress.
Mandatory domain standards: `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `UPSTREAM_TOOLCHAIN.md`; add `AI_DISCOVERY_SEO.md` for editorial/local/search/AI discovery. Google Agent Platform is opt-in only for a distinct agent backend/service. Luma is opt-in only for legitimate creative/editorial generation where real-place/event accuracy is not falsely implied.
Default QA focus: WordPress native architecture, editorial information accuracy/freshness, responsive content, social identity, feed/calendar/event freshness, maps/links, local entity data, search visibility and accessibility.

## @GoAyvalık
Adapter: `projects/goayvalik/AGENTS.md`
Manifest: `projects/goayvalik/PROJECT.md`
Search map: `projects/goayvalik/SEARCH_VISIBILITY.md`
Primary domain: local guide/app/web/product experience.
Hosting/CMS route: Hostinger + WordPress unless a specific surface is verified otherwise.
Mandatory domain standards: `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `UPSTREAM_TOOLCHAIN.md`; add `AI_DISCOVERY_SEO.md` for structured local/place/search/AI discovery. Load `GOOGLE_AGENT_PLATFORM.md` only if GoAyvalık gains a deployable Google ADK/agent-service surface. Luma is optional for promotional creative, never as a source of truth for maps/places/events.
Default QA focus: product UX, responsive web/app surfaces, localization, maps/content freshness, structured place data, brand coherence, search discovery and end-to-end critical flows.

## Specialist pool
Orchestrator may instantiate bounded roles such as Shopify Engineer, WordPress Engineer, Hostinger Deployment Engineer, Browser QA, Visual QA, Accessibility QA, Performance Engineer, SEO Engineer, Entity/Structured Data Specialist, Local SEO Specialist, AI Discovery/GEO Evaluator, Content Strategist, Social Strategist, Instagram Art Director, Graphic Designer, Reels/Video Director, Creative Model Provider Specialist, Reference Fidelity Evaluator, Copywriter, Paid Social Strategist, Performance Analyst, Brand QA, Security Reviewer, Agent Platform Engineer, Google ADK/Agents CLI Specialist, Agent Eval Engineer, Observability Engineer and Strong Advisor.

Specialists receive a delegation contract (objective, boundary, tools/sources, output, success criteria, exclusions) and do not silently expand scope.

## Provider-adapter rule
Provider-specific capabilities are optional adapters, not new constitutions. Google Agents CLI/ADK may be loaded JIT for Google agent-service work; Luma may be loaded JIT for reference-guided image/video generation/editing. Neither may replace the Ercan OS task spec, memory/scope rules, project brand system, independent QA, security boundaries or final completion contract.

A creative provider output is evidence/candidate output, not final approved design. Exact logo/type/layout/product truth and channel requirements remain controlled by `BRAND_SOCIAL.md` + project-local brand assets + independent evaluator.

## Search authority rule
All search/AI-discovery agents prioritize current official platform guidance over third-party GEO scores. Google Search Central, OpenAI crawler/publisher docs, Perplexity crawler docs, Bing/IndexNow docs and Schema.org are authoritative for their respective surfaces. Research/community repos may generate hypotheses and audits but never override platform documentation or justify spam/deceptive tactics.

## Source/hosting rule
Project adapters describe the expected route. Actual live source, hosting account state, Git deployment linkage and platform version must still be inspected at runtime before writes. A project adapter is policy/context, not proof that a deployment is currently connected.

## Future agents
Every new agent inherits the central contract by default. Add it here only when it has a stable routing identity or materially different tool/policy/evaluation contract.
