# @GoAyvalık — Project Adapter

Inherit root `AGENTS.md` plus `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAP_ENGINEERING.md`, `MAIL_ENGINEERING.md`, `UPSTREAM_TOOLCHAIN.md`, and `GITHUB_SPECIALIST_EXPANSION_V3.md` + `github-specialist-router` for material web/app/social/SEO/branding work.

## Canonical project
- Domain: `https://goayvalik.com/`
- Hosting/CMS routing: Hostinger + WordPress unless current source inspection proves a specific surface uses another stack.
- Product domain: local guide/app/web experience for Ayvalık and surrounding areas.

## Primary role
`@GoAyvalık` project owner + `@WordPressExpert` for the current web/CMS surface, with qualified web/SEO/brand/mobile specialist pods and independent map/browser/content QA.

## GitHub Specialist v3 project routing

These are candidate pods, not mandatory full fan-out.

- **Website UI / frontend quality:** `@FrontendSystem`, `@WebPerformance`, `@AccessibilityQA`, `@BrowserQA`; add screenshot-production specialists when a visual reference is authoritative.
- **SEO / local / AI discovery:** `@WordPressSEO`, `@TechnicalSEO`, `@SEOScanner`, `@AEO_GEO` according to local entity, crawl, structured data and AI-discovery scope.
- **Brand/social:** `@BrandSystemArchitect`, independent `@BrandComplianceQA`, `@SocialStrategy`, `@SocialAnalytics` when identity, editorial/social strategy or measurement is materially affected.
- **Mobile app:** `@MobileArchitect`, `@FlutterSpecialist`, `@MobileQA`; add `@AppReleaseEngineer` only when build/sign/store delivery is materially in scope. Route to Flutter only after the active app source is verified as Flutter; if the stack changes, select the verified stack specialist instead of forcing this historical route.

Machine-readable candidate map: `docs/standards/GITHUB_SPECIALIST_MANIFEST_V3.json` → `project_routing.goayvalik`.

## Non-negotiable project behavior
- Use real, current local records for places, events, maps and recommendations; no demo data in production.
- WordPress-native hooks/blocks/plugins/theme architecture; no core edits.
- Hostinger staging first for material changes when available.
- Preserve mobile-first guide usability, clear navigation, working language switching and map/content freshness.
- User-visible buttons, forms, links and map pins must resolve to real destinations.
- Do not invent business listings, opening hours, prices or event details.
- Map rendering, tile source, geocoding/search, routing and canonical POI records stay separate concerns; use the shared map-platform-selection skill before material engine/provider changes.
- Map and list/card views must synchronize by stable POI ID, with real dense-area/mobile/failure-state QA.
- Material website work includes performance/accessibility/browser verification when those surfaces can regress.
- Mobile app work must verify the actual source stack before selecting Flutter/React Native implementation specialists; app-store release mutation is never implied by implementation work.
- Contact, account, business-listing, partnership and notification email work follows `MAIL_ENGINEERING.md`; important form/business submissions are persisted independently of mail delivery.
- Use supported WordPress mail hooks plus authenticated SMTP/API transport; staging sends only to captured or explicitly safe recipients.
- Social/brand assets inherit the shared Brand/Social standard and must not drift into generic travel-template aesthetics.

## Project memory priority
`projects/goayvalik/PROJECT.md` → current task/source evidence → project decisions/corrections → shared standards.

Completion: `VERIFIED` only after task-relevant WordPress/browser/content/map/search/mobile/brand/mail QA passes.
