# @AyvalıkVibes — Project Adapter

Inherit root `AGENTS.md` plus `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAP_ENGINEERING.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`, and `GITHUB_SPECIALIST_EXPANSION_V3.md` + `github-specialist-router` for material web/social/SEO/branding work.

## Canonical project
- Website: https://ayvalikvibes.com/
- Hosting/CMS routing: Hostinger + WordPress.
- Domain: editorial/local guide, events, maps, blog, local commerce/partnerships and social media.

## Primary role
`@AyvalıkVibes` project owner + `@WordPressExpert` platform owner with qualified editorial/web/SEO/social/brand specialist pods and independent QA.

## GitHub Specialist v3 project routing

These are candidate pods; select only materially required specialists.

- **Website UI / frontend quality:** `@FrontendSystem`, `@WebPerformance`, `@AccessibilityQA`, `@BrowserQA`; add screenshot-production specialists for reference-led UI work.
- **SEO / local / AI discovery:** `@WordPressSEO`, `@TechnicalSEO`, `@SEOScanner`, `@AEO_GEO` according to crawl, structured local entity, editorial discovery and AI-search scope.
- **Brand system:** `@BrandSystemArchitect`, `@DesignTokenArchitect`, independent `@BrandComplianceQA` when reusable identity/tokens/cross-channel consistency is materially affected.
- **Social:** `@SocialStrategy`, `@SocialPublishingOps`, `@SocialAnalytics`, `@ContentRecycling` according to strategy, scheduling/publishing, analytics and editorial reuse scope. Publishing requires authenticated provider capability and is never implied by content creation.

Machine-readable candidate map: `docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json` → `project_routing.ayvalik-vibes`.

## Non-negotiable project behavior
- Content accuracy/freshness matters: dates, events, venues, prices, map/location and external source claims are verified when time-sensitive.
- WordPress-native block/theme/plugin architecture; never edit core.
- Site-critical functionality belongs in plugin/custom application logic rather than being trapped in presentation-only theme code.
- Hostinger staging first for material changes when available.
- Preserve the warm, clean Ayvalık/Cunda editorial identity; do not make the site/social feed generically dark, SaaS-like or AI-template-like without explicit direction.
- Instagram/feed/calendar assets must be mobile readable and platform-safe; old event data must not be represented as current.
- Maps, links, recommendation records and commerce/legal flows require real destinations/data; no demo placeholders in production.
- Map rendering, tile source, geocoding/search and canonical POI/editorial records are separate concerns; use `MAP_ENGINEERING.md` + the map-platform-selection skill for material map/provider changes.
- Map UI must have an accessible list/detail equivalent and be tested for list↔pin sync, mobile overlays, attribution and failure states.
- Material website work includes performance/accessibility/browser verification when those surfaces can regress.
- Search/AI-discovery work never promises ranking or recommendation placement; current entity/freshness evidence remains authoritative.
- Contact, partnership, sponsor, newsletter and form-notification email work follows `MAIL_ENGINEERING.md`; important submissions are persisted before/alongside notification so temporary email failure does not lose them.
- Marketing/newsletter sends require explicit list/consent/unsubscribe handling and must not be implemented as synchronous loops in WordPress requests.
- Staging mail is captured or restricted to safe test recipients; no production subscriber/customer list is used for QA.

## Project memory priority
`projects/ayvalik-vibes/PROJECT.md` → current source/freshness evidence → project decisions/corrections → shared standards.

Completion: `VERIFIED` only after platform QA and, for task-relevant work, freshness/source/map/search/social/brand/mail checks pass.
