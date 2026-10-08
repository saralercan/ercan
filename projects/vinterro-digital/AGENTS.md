# @VinterroDigital — Project Adapter

Inherit root `AGENTS.md` plus `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`, and `GITHUB_SPECIALIST_EXPANSION_V3.md` + `github-specialist-router` for material web/social/SEO/Meta/branding work.

## Canonical project
- Website: https://vinterro.digital/
- Hosting/CMS: Hostinger + WordPress for project routing unless current account/source inspection proves a specific surface uses another stack.

## Primary role
`@VinterroDigital` project owner + `@WordPressExpert` platform owner with qualified brand/web/social/SEO/Meta specialist pods and independent QA.

## GitHub Specialist v3 project routing

These are candidate pods; Orchestrator still applies material-contribution filtering.

- **Website UI / frontend quality:** `@FrontendSystem`, `@WebPerformance`, `@AccessibilityQA`, `@BrowserQA`; add screenshot-production specialists for reference-led reproduction. For reference-led WordPress theme reconstruction/migration, load `@WordPressReplica` JIT via `.agents/skills/wordpress-replica/SKILL.md`.
- **SEO / AI discovery:** `@WordPressSEO`, `@TechnicalSEO`, `@SEOScanner`, `@AEO_GEO` according to platform/crawl/entity/AI-discovery scope.
- **Brand system / cross-channel identity:** `@BrandSystemArchitect`, `@BrandBehavior`, `@DesignTokenArchitect`, `@BrandRuntimeEngineer`, independent `@BrandComplianceQA` according to reusable brand-system scope.
- **Social:** `@SocialStrategy`, `@SocialPublishingOps`, `@SocialAgentOps`, `@SocialAnalytics`, `@ContentRecycling` according to strategy, publishing, agent-operated workflow, analytics and reuse scope. Authenticated publishing is never inferred from content creation.
- **Meta paid media:** `@AdsCreativeStrategist`, `@MetaAdsEngineer`, `@MetaMeasurement`, `@MarketingScience`, `@IncrementalityAnalyst` according to creative-test, campaign execution, Pixel/CAPI, allocation/MMM or causal-lift needs.

Machine-readable candidate map: `docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json` → `project_routing.vinterro-digital`.

## Non-negotiable project behavior
- Preserve the approved Vinterro Digital identity and current user-approved visual direction.
- Do not change logo/site-wide design when the request is scoped to copy or one component.
- Distinctive agency craft over generic AI/template aesthetics.
- WordPress-native hooks/blocks/theme/plugin architecture; never edit core and avoid vendor/plugin source patches.
- Hostinger staging/preview first for material production changes when available.
- Git/source reconciliation before linking/deploying over unmanaged live files.
- Material website work includes performance/accessibility/browser verification when those surfaces can regress.
- Instagram organic, paid, feed, Reels/Stories and logo work follow `BRAND_SOCIAL.md`; mobile/feed preview and export QA required.
- Paid creative requires objective, audience, offer, hook/angle, proof, CTA, placement and measurement hypothesis.
- **Measurement-only** Meta tasks remain read-only with respect to campaign/ad-set/ad mutation unless campaign execution is separately and explicitly in scope.
- Attribution/ROAS is not causal-lift proof; use `@IncrementalityAnalyst` only when causal lift is actually the question.
- Contact, proposal, lead, outreach and website-notification email work follows `MAIL_ENGINEERING.md`; important leads are persisted/correlated independently of notification email so provider failure cannot lose the enquiry.
- **Sales intelligence / prospect discovery:** use `Sales Intelligence Agent / @SalesIntelligence` with `docs/standards/VINTERRO_SALES_INTELLIGENCE_AGENT.md` and the four Sales Intelligence skills for company discovery, public-business enrichment, missing/broken website opportunity audits, account-level dedupe and qualification/scoring. The agent is read-only with respect to outbound actions; qualified accounts hand off to Outreach/MailAgent under the existing first-touch gates.
- Vinterro Digital first-touch outreach also loads `.agents/skills/vinterro-mail-agent/SKILL.md`, `docs/standards/VINTERRO_OUTREACH_SCHEDULE.md`, `docs/standards/VINTERRO_MAIL_AGENT.md` **and** the exact source artifact `docs/standards/VINTERRO_MAIL_CANONICAL_TEMPLATE.html`. `mail ajanı` / `@MailAgent` owns execution, Gmail dedupe, delivery truth and quota accounting; `metin ajanı` / `@TextAgent` owns evidence-grounded outreach copy, localization and copy QA. Both must use the same canonical 08:00/20:00 regional schedule and may not create parallel outreach rules. The wrapper/signature may never be reconstructed from memory or approximated; if the canonical template cannot be loaded, rendering/sending is BLOCKED.
- **Mail body, copy behavior and signature are project standards.** Body content is personalized per prospect, but must follow the canonical Vinterro copy contract (business-first, verified observation, narrow commercial angle, relevant web action, Google/Meta only when justified, one low-friction CTA). The HTML geometry and signature are locked exactly to `VINTERRO_MAIL_CANONICAL_TEMPLATE.html`. Any 760/780px near-match, altered padding/line-height/divider/signature typography, centered body, decorative card/background or hand-written signature variant must fail MailQA before send.
- **Account-level atomic dedupe is mandatory before every first-touch send.** Recipient email is not account identity. Resolve business/brand + location + canonical/current and previous domains + aliases + all known emails + store/booking URLs + Gmail history, then acquire a claim in `public.vinterro_outreach_account_claims` immediately before send. Any account/domain/name+location/email conflict blocks send. A different mailbox for the same business never bypasses suppression. If the live claim store is unavailable, production first-touch send is BLOCKED; research/drafting may continue. Parallel agents may research in parallel but may not send without independent atomic claims.
- **Provider ambiguity never permits automatic retry.** Every production first-touch must obtain a token from `public.vinterro_prepare_first_touch(...)`; SENT must be finalized with `public.vinterro_finalize_first_touch_sent(...)`. If the send/tool result is timeout/error/unknown, lock it with `public.vinterro_mark_first_touch_ambiguous(...)` and do not retry until Gmail SENT/thread reconciliation proves no send and `public.vinterro_release_first_touch_after_no_send(...)` records that proof. No token = no send; ambiguous = no retry.
- Bounced, delayed, obsolete-domain or ambiguous outreach contacts route to the live `Contact Recovery Research Agent` and `docs/standards/VINTERRO_CONTACT_RECOVERY_RESEARCH.md`. The agent must research official web + redirects/new domains + Instagram + Facebook + LinkedIn + Google Business/Maps evidence + booking/operator + credible tourism/chamber records before a recovered address is considered clean. It is read-only; MailAgent retains send/dedupe/suppression/delivery authority.
- WordPress/Hostinger mail uses supported WordPress hooks/APIs plus authenticated SMTP/API transport; no core PHPMailer edits, raw credential exposure or production-list sends from staging.
- Sender identity, reply-to, brand template, delivery status and safe test-recipient evidence are part of completion for material mail changes.

## Project memory priority
`projects/vinterro-digital/PROJECT.md` → current task evidence → approved GOOD/BAD brand references/corrections → shared standards.

Completion: `VERIFIED` only after the task-relevant brand/platform/browser/export/search/measurement/mail QA passes.

## Web Builder Capability Pack
For material website generation/modernization, visual editing, WordPress engineering/theme QA, localization, media optimization, PWA/offline, frontend-health, browser-operator or web-security work, load `.agents/skills/web-builder-capability-pack/SKILL.md`. For screenshot/mockup/Figma/HTML/reference-led WordPress work, additionally load `.agents/skills/wordpress-replica/SKILL.md` + `docs/standards/WORDPRESS_REPLICA_ENGINE.md`; the `@WordPressReplica` alias resolves to existing stable specialists. Keep `@WordPressExpert` as the platform owner for the verified WordPress surface and retain Hostinger deployment as a separate boundary when deployment is actually in scope.
