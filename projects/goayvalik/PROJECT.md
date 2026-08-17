# GoAyvalık Project Manifest

- Agent: `@GoAyvalık`
- Domain: `https://goayvalik.com/`
- Platform routing: Hostinger + WordPress
- Product: local guide/app/web experience for Ayvalık and surrounding areas.

## Priority surfaces
- guide/navigation
- places and location records
- maps
- events/content
- multilingual pages
- membership/account features when active
- local shop/partnership features when active
- social/brand assets

## Rules
- Verify current local data before publication.
- No WordPress core edits; use supported hooks/blocks/plugins/theme patterns.
- Reconcile production files before Git deployment to an existing Hostinger WordPress installation.
- Use staging first for material changes where available.
- Test mobile navigation, language switching, maps, forms and primary CTAs.
- Do not invent listings, map pins, events, hours, prices or reviews.

## QA
Use task-relevant WPCS/PHPCS, build/runtime checks, WordPress smoke, Playwright critical flows, responsive/visual QA, accessibility, performance, localization and content/map freshness checks.

The central Ercan OS repo currently provides governance and project routing. When the verified site source is connected to GitHub, that source repo should carry a small local adapter inheriting this contract.
