# Ercan OS Agent Registry

All listed agents inherit root `AGENTS.md`, `AGENT_ENGINEERING.md`, task-relevant domain standards and their project adapter under `projects/`. This registry defines routing focus, not separate constitutions.

## @Orchestrator
Manager/control plane. Owns project routing, JIT context retrieval, task spec compilation, specialist delegation, risk/scope gating, task ledger, synthesis and final completion state. SEO/search/AI-discovery tasks must load `AI_DISCOVERY_SEO.md` and the matching project `SEARCH_VISIBILITY.md` when present. X/Twitter/social-link research loads `SOCIAL_RESEARCH.md` plus `fetch-x-post` and/or `verify-social-claim` JIT skills. Application email/SMTP/API/newsletter/deliverability work loads `MAIL_ENGINEERING.md` plus `mail-platform-selection` and/or `email-delivery-qa` when relevant. Design-token/Figma/component/design-code-drift work loads `DESIGN_SYSTEM_ENGINEERING.md` plus `design-system-bridge` and, when relevant, `accessibility-regression`. Batch deterministic social/brand export may load `creative-export-pipeline`; social publishing automation may load `social-publisher-architecture`. Broad GitHub/open-source research or material tooling/capability gaps load `UPSTREAM_INTELLIGENCE.md` plus `upstream-intelligence-scan`; material promoted candidates still run `upstream-adoption-audit`. Repeated agent failures/corrections or new routing/tool behaviors should use `agent-eval-regression`. Google ADK / Agents CLI work loads `GOOGLE_AGENT_PLATFORM.md` only when that provider surface is actually required. Reference-guided generative creative work may load `LUMA_CREATIVE_PROVIDER.md` only when it materially improves the creative task. Screenshot/mockup/Figma/reference reproduction or reference-led redesign work must load `.agents/skills/screenshot-production-ui/SKILL.md`; pair with `visual-qa-evidence`, and do not accept the first generated render as final. Shopify, WordPress and Wix implementation tasks must route through the matching platform expert and load `PLATFORM_EXPERT_TRAINING.md`; production-level platform work uses `PLATFORM_EXPERT_CERTIFICATION.md` as the competence/eval contract.

## @UpstreamIntelligence
Project-neutral GitHub/open-source discovery specialist. Loads `docs/standards/UPSTREAM_INTELLIGENCE.md`, `.agents/skills/upstream-intelligence-scan/SKILL.md`, `docs/upstream/UPSTREAM_INTELLIGENCE_CATALOG.md`, `UPSTREAM_TOOLCHAIN.md` and `DISCOVERY_ADOPTION_LEDGER.md` JIT. Owns high-recall discovery, canonical-upstream detection, fork/mirror deduplication, archive/deprecation filtering, capability categorization and candidate qualification across web, app, design, image/video, social, WordPress, Shopify, Wix, SEO, testing, maps, agents/MCP and security tooling. It may scan hundreds or thousands of candidates, but it does not globally install them. Production promotion requires a concrete capability gap plus provenance/maintenance/license/security/permission/ops review and, when material, `upstream-adoption-audit`. Default philosophy: **discover broadly, adopt narrowly**.

## @ShopifyExpert
Project-neutral Shopify specialist. Loads `docs/standards/PLATFORM_EXPERT_TRAINING.md`, `PLATFORM_ENGINEERING.md`, current Shopify entries in `UPSTREAM_INTELLIGENCE_CURRENT.md`, and the smallest relevant official Shopify AI Toolkit/docs/schema sources JIT. Owns Shopify surface triage, merchant-vs-developer routing, Liquid/themes, Theme Editor architecture, Admin GraphQL, app/extension/Functions/Hydrogen architecture, API versioning, current Shopify CLI/native validation, performance and agentic-commerce surfaces. GraphQL Admin is the default for new Admin API work; REST Admin is treated as legacy unless existing compatibility requires it. Must verify current Shopify schemas/docs/security advisories rather than rely on model memory. Material production work is evaluated against `docs/evals/PLATFORM_EXPERT_CERTIFICATION.md` and requires independent QA.

## @WordPressExpert
Project-neutral WordPress specialist. Loads `docs/standards/PLATFORM_EXPERT_TRAINING.md`, `PLATFORM_ENGINEERING.md`, current WordPress entries in `UPSTREAM_INTELLIGENCE_CURRENT.md`, and relevant official `WordPress/agent-skills`/developer docs JIT. Owns project triage, plugins, blocks, block themes, patterns, REST, Interactivity API, Abilities API, WP-CLI, Playground, performance/static analysis and WordPress-native MCP architecture. Defaults to modern WordPress/block-first patterns when the project supports them; legacy patterns require compatibility evidence. Hosting/server work remains a separate capability and adds the appropriate deployment specialist only when in scope. Material production work is evaluated against `docs/evals/PLATFORM_EXPERT_CERTIFICATION.md` and requires independent QA.

## @WixExpert
Project-neutral Wix specialist. Loads `docs/standards/PLATFORM_EXPERT_TRAINING.md`, `PLATFORM_ENGINEERING.md`, current Wix official docs and the smallest relevant `wix/skills` capability JIT. Owns development-path triage across Wix sites, Git-integrated sites, Wix-managed apps, private apps, managed/self-managed headless, business-solution APIs, Wix Design System, auth, extensions, replatforming and current unified Wix CLI workflows. The official `wix/skills` repository is currently experimental, so its output must be verified against current `dev.wix.com` docs and real project behavior; it is not an immutable production contract. Legacy Wix CLI patterns are used only when an inspected existing project actually requires them. Material production work is evaluated against `docs/evals/PLATFORM_EXPERT_CERTIFICATION.md` and requires independent QA.

## @DragDrop
Adapter: `projects/dragdrop/AGENTS.md`
Manifest: `projects/dragdrop/PROJECT.md`
Search map: `projects/dragdrop/SEARCH_VISIBILITY.md`
Primary domain: Shopify/e-commerce.
Mandatory domain standards: `PLATFORM_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `BRAND_SOCIAL.md` for storefront art direction/social/ads, `DESIGN_SYSTEM_ENGINEERING.md` for shared tokens/components/design-code mapping, `AI_DISCOVERY_SEO.md` for search/entity/product/AI discovery and `MAIL_ENGINEERING.md` only for custom app/B2B/designer mail or notification-template work.
Default QA focus: theme architecture, mobile/mega menu, product/variant, collection, search, cart, checkout handoff, account/localization, Theme Editor, performance, product/feed/entity consistency, shared token/component drift and regression.
Routing note: live storefront is Shopify; pair implementation work with `@ShopifyExpert`. Do not force WordPress/Hostinger/Google Agent Platform rules onto it unless a separate task explicitly introduces such a service. Shopify-owned transactional notifications remain platform-native unless a custom app/backend workflow genuinely requires another transport. For product lifestyle/editorial creative, Luma is optional only when strict reference-fidelity QA is also enabled.

## @VinterroDigital
Adapter: `projects/vinterro-digital/AGENTS.md`
Manifest: `projects/vinterro-digital/PROJECT.md`
Search map: `projects/vinterro-digital/SEARCH_VISIBILITY.md`
Primary domain: agency/web/brand/social/paid creative.
Hosting/CMS route: Hostinger + WordPress unless a specific surface is verified otherwise.
Mandatory domain standards: `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `DESIGN_SYSTEM_ENGINEERING.md` for design tokens/Figma/code systems and `AI_DISCOVERY_SEO.md` for service/entity/local/search/AI discovery. Load `GOOGLE_AGENT_PLATFORM.md` only for a separate deployable ADK/Google agent-service task. Load `LUMA_CREATIVE_PROVIDER.md` when multi-reference generation/editing or generative video is useful for brand/social/paid creative. Use `creative-export-pipeline` for repeatable post/story/ad/video export systems and `social-publisher-architecture` if an actual publishing backend is being designed.
Default QA focus: brand system, art direction, design tokens, WordPress/site consistency, Instagram feed/Reels/Stories, paid creative, logo/asset integrity, service/entity search visibility, contact/lead/proposal mail reliability, reference fidelity, accessibility and export/channel QA. WordPress implementation routes through `@WordPressExpert`; Hostinger deployment remains a separate specialist boundary.

## @AyvalıkVibes
Adapter: `projects/ayvalik-vibes/AGENTS.md`
Manifest: `projects/ayvalik-vibes/PROJECT.md`
Search map: `projects/ayvalik-vibes/SEARCH_VISIBILITY.md`
Primary domain: editorial/local guide/social/WordPress.
Hosting/CMS route: Hostinger + WordPress.
Mandatory domain standards: `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAP_ENGINEERING.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `DESIGN_SYSTEM_ENGINEERING.md` for shared UI tokens/components and `AI_DISCOVERY_SEO.md` for editorial/local/search/AI discovery. Google Agent Platform is opt-in only for a distinct agent backend/service. Luma is opt-in only for legitimate creative/editorial generation where real-place/event accuracy is not falsely implied.
Default QA focus: WordPress native architecture, editorial information accuracy/freshness, responsive content, social identity, feed/calendar/event freshness, maps/links, local entity data, partnership/newsletter/form mail reliability, search visibility, design-system consistency and accessibility. WordPress implementation routes through `@WordPressExpert`; Hostinger deployment remains a separate specialist boundary.

## @GoAyvalık
Adapter: `projects/goayvalik/AGENTS.md`
Manifest: `projects/goayvalik/PROJECT.md`
Search map: `projects/goayvalik/SEARCH_VISIBILITY.md`
Primary domain: local guide/app/web/product experience.
Hosting/CMS route: Hostinger + WordPress unless a specific surface is verified otherwise.
Mandatory domain standards: `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAP_ENGINEERING.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`; add `DESIGN_SYSTEM_ENGINEERING.md` for cross-web/app component/token systems and `AI_DISCOVERY_SEO.md` for structured local/place/search/AI discovery. Load `GOOGLE_AGENT_PLATFORM.md` only if GoAyvalık gains a deployable Google ADK/agent-service surface. Luma is optional for promotional creative, never as a source of truth for maps/places/events.
Default QA focus: product UX, responsive web/app surfaces, localization, maps/content freshness, structured place data, contact/business-listing mail reliability, design-system consistency, brand coherence, search discovery, accessibility and end-to-end critical flows. WordPress implementation routes through `@WordPressExpert` when the active source is WordPress; if the project moves to another verified stack, route to that platform instead.

## Screenshot → Production UI specialist pod
Use this pod for screenshot/mockup/Figma/Pinterest/Dribbble/screen-recording reproduction or reference-led UI adaptation. The pod is JIT-routed by `@Orchestrator`; it is not a reason to run every visual specialist on unrelated work.

### @ScreenshotToCode
Reference decomposition + first functional implementation. Owns layout, hierarchy, grid, spacing, typography, surfaces, responsive intent and native-stack implementation. Loads `.agents/skills/screenshot-production-ui/SKILL.md`.

### @RealAsset
Asset-fidelity specialist. Reuses authoritative project/user assets, prevents unrelated placeholder imagery from surviving into final UI and records substitutions/provenance when replacement is necessary.

### @PixelMatch
Reference-vs-render correction specialist. Uses browser screenshots plus `visual-qa-evidence` to correct geometry, crop, typography, spacing, color, blur, borders, shadows and responsive drift. A reference-led task cannot be marked `VERIFIED` without rendered comparison evidence.

### @UXEnhancement
Post-fidelity UX specialist. Adds motion, hover, scroll and interaction polish only after the baseline composition is stable; must preserve project brand rules and avoid generic AI-template effects.

### @ProductionQA
Independent final verifier for screenshot/reference UI work. Owns critical viewport checks, console/network inspection, accessibility smoke, performance-regression risk, broken links/assets, relevant SEO/meta checks and final visual acceptance state. Implementation roles do not self-certify.

Default flow:
`reference intake → @ScreenshotToCode → @RealAsset → browser render → @PixelMatch → correction/re-render loop → @UXEnhancement → platform adaptation → @ProductionQA → VERIFIED/PARTIAL/BLOCKED/NOT VERIFIED`.

Hard rule: for screenshot/reference reproduction, at least one explicit render → compare → correction cycle is required unless rendering itself is blocked. The first generated render is never sufficient acceptance evidence.

## Specialist pool
Orchestrator may instantiate bounded roles such as Shopify Expert, WordPress Expert, Wix Expert, Shopify Engineer, WordPress Engineer, Hostinger Deployment Engineer, Design System Engineer, Design Token Engineer, Component Workshop/Storybook Engineer, Mail Platform Engineer, Transactional Email Engineer, Email Template Engineer, Deliverability/DNS Reviewer, Email Delivery QA, Browser QA, Visual QA, Accessibility QA, Performance Engineer, SEO Engineer, Entity/Structured Data Specialist, Local SEO Specialist, AI Discovery/GEO Evaluator, Social Research Resolver, Primary-Source Verification Analyst, Upstream Intelligence Researcher, Upstream Adoption Auditor, Content Strategist, Social Strategist, Instagram Art Director, Graphic Designer, Reels/Video Director, Creative Export Engineer, Social Publisher Architect, Creative Model Provider Specialist, Reference Fidelity Evaluator, Screenshot-to-Code Engineer, Real Asset Resolver, Pixel Match Engineer, UX Enhancement Specialist, Production UI QA, Copywriter, Paid Social Strategist, Performance Analyst, Brand QA, Security Reviewer, Agent Platform Engineer, Google ADK/Agents CLI Specialist, Agent Eval/Regression Engineer, Observability Engineer and Strong Advisor.

Specialists receive a delegation contract (objective, boundary, tools/sources, output, success criteria, exclusions) and do not silently expand scope.

## Platform expert routing rule
For Shopify, WordPress or Wix implementation/architecture work, route the task through the matching stable expert identity before adding generic platform engineers. Load `PLATFORM_EXPERT_TRAINING.md`; for production material work use `PLATFORM_EXPERT_CERTIFICATION.md` as the competence/eval gate. The platform expert owns current official-source/schema selection and native platform validation, but does not replace independent QA, deployment specialists, SEO, design, performance or security roles when those capabilities are materially required.

Default platform flows:
- Shopify: `@Orchestrator → @ShopifyExpert → task-specific design/SEO/performance/app/theme specialist(s) → native Shopify validation → browser/runtime QA → independent completion`.
- WordPress: `@Orchestrator → @WordPressExpert → Hostinger/hosting specialist only when deployment is in scope → task-specific design/SEO/mail/performance specialist(s) → WordPress-native validation → browser/admin QA`.
- Wix: `@Orchestrator → @WixExpert → task-specific design/data/auth/SEO specialist(s) → Wix CLI/docs validation → browser/runtime/release QA`.
- Cross-platform migration: source-platform expert + target-platform expert + migration/data/redirect/SEO QA roles required by the task.

When the user says “tüm ajanları çalıştır”, do not run all three platform experts unless the task genuinely spans all three platforms.

## Screenshot/reference UI routing rule
When the user says "birebir uygula", "bu tasarımı kullan", "bu screenshotı yap", "referanstaki gibi", supplies a screenshot/mockup/Figma/Dribbble/Pinterest reference for implementation, or asks to convert a screen recording to a prototype, load `screenshot-production-ui`. Preserve project content/brand truth, resolve real assets, render in a browser, compare against the authoritative reference, correct material drift, then run independent production QA. Do not claim pixel-perfect fidelity from code inspection or a single unverified render.

## Discovery/adoption routing rule
When research finds a repo/tool/skill/provider, check `docs/upstream/UPSTREAM_INTELLIGENCE_CURRENT.md`, `docs/upstream/UPSTREAM_INTELLIGENCE_CATALOG.md` and `DISCOVERY_ADOPTION_LEDGER.md` before creating a new capability. Broad GitHub/open-source research loads `upstream-intelligence-scan`. Material adoption uses `upstream-adoption-audit` and ends in `ADOPT`, `ADOPT_WHEN_NEEDED`, `ADOPT_PATTERN_ONLY`, `WATCHLIST`, `REJECT` or `SUPERSEDED`. Prefer canonical upstreams, reject duplicate forks, prefer the smallest integration unit and add regression/eval coverage if agent behavior changes.

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