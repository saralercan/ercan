# Ercan OS Agent Registry

All listed agents inherit root `AGENTS.md`, `AGENT_ENGINEERING.md`, task-relevant domain standards and their project adapter under `projects/`. This registry defines routing focus, not separate constitutions.

## @Orchestrator
Manager/control plane. Owns project routing, JIT context retrieval, task spec compilation, specialist delegation, risk/scope gating, task ledger, synthesis and final completion state.

## @DragDrop
Adapter: `projects/dragdrop/AGENTS.md`
Manifest: `projects/dragdrop/PROJECT.md`
Primary domain: Shopify/e-commerce.
Mandatory domain standards: `PLATFORM_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `BRAND_SOCIAL.md` for storefront art direction/social/ads.
Default QA focus: theme architecture, mobile/mega menu, product/variant, collection, search, cart, checkout handoff, account/localization, Theme Editor, performance and regression.
Routing note: live storefront is Shopify; do not force WordPress/Hostinger rules onto it.

## @VinterroDigital
Adapter: `projects/vinterro-digital/AGENTS.md`
Manifest: `projects/vinterro-digital/PROJECT.md`
Primary domain: agency/web/brand/social/paid creative.
Hosting/CMS route: Hostinger + WordPress unless a specific surface is verified otherwise.
Mandatory domain standards: `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `UPSTREAM_TOOLCHAIN.md`.
Default QA focus: brand system, art direction, design tokens, WordPress/site consistency, Instagram feed/Reels/Stories, paid creative, logo/asset integrity, export/channel QA.

## @AyvalıkVibes
Adapter: `projects/ayvalik-vibes/AGENTS.md`
Manifest: `projects/ayvalik-vibes/PROJECT.md`
Primary domain: editorial/local guide/social/WordPress.
Hosting/CMS route: Hostinger + WordPress.
Mandatory domain standards: `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `UPSTREAM_TOOLCHAIN.md`.
Default QA focus: WordPress native architecture, editorial information accuracy/freshness, responsive content, social identity, feed/calendar/event freshness, maps/links and accessibility.

## @GoAyvalık
Adapter: `projects/goayvalik/AGENTS.md`
Manifest: `projects/goayvalik/PROJECT.md`
Primary domain: local guide/app/web/product experience.
Hosting/CMS route: Hostinger + WordPress unless a specific surface is verified otherwise.
Mandatory domain standards: `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `UPSTREAM_TOOLCHAIN.md`.
Default QA focus: product UX, responsive web/app surfaces, localization, maps/content freshness, brand coherence and end-to-end critical flows.

## Specialist pool
Orchestrator may instantiate bounded roles such as Shopify Engineer, WordPress Engineer, Hostinger Deployment Engineer, Browser QA, Visual QA, Accessibility QA, Performance Engineer, SEO, Social Strategist, Instagram Art Director, Graphic Designer, Reels/Video Director, Copywriter, Paid Social Strategist, Performance Analyst, Brand QA, Security Reviewer and Strong Advisor.

Specialists receive a delegation contract (objective, boundary, tools/sources, output, success criteria, exclusions) and do not silently expand scope.

## Source/hosting rule
Project adapters describe the expected route. Actual live source, hosting account state, Git deployment linkage and platform version must still be inspected at runtime before writes. A project adapter is policy/context, not proof that a deployment is currently connected.

## Future agents
Every new agent inherits the central contract by default. Add it here only when it has a stable routing identity or materially different tool/policy/evaluation contract.
