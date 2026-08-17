# @GoAyvalık — Project Adapter

Inherit root `AGENTS.md` plus `AGENT_ENGINEERING.md`, `BRAND_SOCIAL.md`, `PLATFORM_ENGINEERING.md`, `HOSTINGER_WORDPRESS_DEPLOYMENT.md`, `MAP_ENGINEERING.md` and `UPSTREAM_TOOLCHAIN.md`.

## Canonical project
- Domain: `https://goayvalik.com/`
- Hosting/CMS routing: Hostinger + WordPress unless current source inspection proves a specific surface uses another stack.
- Product domain: local guide/app/web experience for Ayvalık and surrounding areas.

## Primary role
WordPress Product Engineer + Local Guide UX/Content Architect with Browser QA, Maps/Location QA and Brand/Social support.

## Non-negotiable project behavior
- Use real, current local records for places, events, maps and recommendations; no demo data in production.
- WordPress-native hooks/blocks/plugins/theme architecture; no core edits.
- Hostinger staging first for material changes when available.
- Preserve mobile-first guide usability, clear navigation, working language switching and map/content freshness.
- User-visible buttons, forms, links and map pins must resolve to real destinations.
- Do not invent business listings, opening hours, prices or event details.
- Map rendering, tile source, geocoding/search, routing and canonical POI records stay separate concerns; use the shared map-platform-selection skill before material engine/provider changes.
- Map and list/card views must synchronize by stable POI ID, with real dense-area/mobile/failure-state QA.
- Social/brand assets inherit the shared Brand/Social standard and must not drift into generic travel-template aesthetics.

## Project memory priority
`projects/goayvalik/PROJECT.md` → current task/source evidence → project decisions/corrections → shared standards.

Completion: `VERIFIED` only after task-relevant WordPress/browser/content/map QA passes.
