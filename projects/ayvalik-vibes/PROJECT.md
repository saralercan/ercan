# Ayvalık Vibes Project Manifest

- Agent: `@AyvalıkVibes`
- Website: `https://ayvalikvibes.com/`
- Platform: Hostinger + WordPress
- Scope: editorial, local guides, events, maps, social media, partnerships and active commerce surfaces.

## Rules
- Verify dates, venues, prices, locations and other time-sensitive facts before publishing.
- Do not present past events as current.
- Use WordPress-native hooks, blocks, plugins and theme architecture; do not edit WordPress core.
- Reconcile live files before connecting or deploying Git over an existing production WordPress installation.
- Test user-facing navigation, forms, maps and links against real destinations.
- Social assets must follow Ayvalık Vibes brand rules and pass mobile/feed preview checks.

## QA
Use task-relevant WPCS/PHPCS, build/runtime checks, WordPress smoke tests, Playwright, responsive visual QA, accessibility, performance, content-freshness checks and post-deploy smoke.

The central Ercan OS repo stores project governance. When the verified WordPress source is connected to GitHub, keep custom code there and retain this project adapter as the shared operating contract.
