# @AyvalıkVibes — Project Adapter

Inherit root `AGENTS.md` plus `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAP_ENGINEERING.md`, `MAIL_ENGINEERING.md` and `UPSTREAM_TOOLCHAIN.md`.

## Canonical project
- Website: https://ayvalikvibes.com/
- Hosting/CMS routing: Hostinger + WordPress.
- Domain: editorial/local guide, events, maps, blog, local commerce/partnerships and social media.

## Primary role
WordPress Editorial Product Engineer + Social/Brand Director with SEO/content freshness and Browser QA support.

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
- Contact, partnership, sponsor, newsletter and form-notification email work follows `MAIL_ENGINEERING.md`; important submissions are persisted before/alongside notification so temporary email failure does not lose them.
- Marketing/newsletter sends require explicit list/consent/unsubscribe handling and must not be implemented as synchronous loops in WordPress requests.
- Staging mail is captured or restricted to safe test recipients; no production subscriber/customer list is used for QA.

## Project memory priority
`projects/ayvalik-vibes/PROJECT.md` → current source/freshness evidence → project decisions/corrections → shared standards.

Completion: `VERIFIED` only after platform QA and, for time-sensitive content or mail work, freshness/source/mail checks pass.
