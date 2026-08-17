# Vinterro Digital Project Manifest

## Identity
- Agent alias: `@VinterroDigital`
- Canonical website: `https://vinterro.digital/`
- Project routing platform: Hostinger + WordPress unless a specific surface is verified otherwise at runtime.
- Business domain: growth marketing, web, social, branding, advertising and creative production.

## Core product surfaces
- website/CMS
- service and proposal/contact flows
- brand system and design tokens
- Instagram feed, Stories, Reels and paid social creative
- logo/identity assets
- customer-facing proposal/presentation/email creative when in scope

## Production guardrails
- Existing approved logo/identity is authoritative; do not invent replacement marks without an explicit logo task.
- If task says “only change copy”, preserve logo, layout, colors, component structure and unrelated pages.
- Use WordPress-native architecture; no core edits.
- For Hostinger deployment, stage/test first where supported and keep a rollback point.
- Do not connect Git deployment over a live unmanaged WordPress directory until source reconciliation is complete.
- Generated creative is not final until mobile/channel preview, copy proof, brand QA and export QA pass.
- Claims/case studies/testimonials must be source-backed; no fabricated proof.

## QA baseline
Website: WPCS/PHPCS where applicable, build, runtime activation/smoke, Playwright critical flows, responsive/visual QA, accessibility, performance and post-deploy smoke.
Creative: brand fit, hierarchy, originality, craft, message clarity, channel fit, safe zones, logo/asset integrity and export correctness.

## Source-state note
The central Ercan OS repository currently stores governance/project adapters, not a verified full copy of the live WordPress codebase. When Hostinger/GitHub source sync is established, the source repo becomes the code source of truth; live database/media remain environment state and require a separate backup/migration policy.
