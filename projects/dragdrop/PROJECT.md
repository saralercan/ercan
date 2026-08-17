# DragDrop Project Manifest

## Identity
- Agent alias: `@DragDrop`
- Canonical storefront: `https://www.draganddrop.tr/`
- Secondary app/account domain observed from storefront: `https://www.draganddrop.online/`
- Platform classification: Shopify commerce/storefront.

## Current engineering priorities
- Shopify theme architecture and merchant editability
- responsive header/mega menu/mobile menu
- designers and designer-profile templates
- product/card/collection consistency
- search, account and cart UX
- B2B/kurumsal flows where explicitly in scope
- performance and accessibility
- SEO/content without breaking commerce behavior

## Production guardrails
- No WordPress assumptions for the Shopify storefront.
- No direct live-theme patch without first inspecting current state and preserving rollback.
- No product/collection/designer data mutation unless task explicitly requires it.
- Payment/customer/checkout changes receive elevated review.
- User screenshots/references are task evidence and should be reproduced at critical viewports before declaring success.

## QA baseline
For affected flows select from: Theme Check, build/schema validation, Shopify preview/development theme, Playwright/browser QA, 390/430/768/1440 responsive checks, console/network inspection, accessibility smoke, performance regression and post-publish smoke.

## Source-state note
The central Ercan OS repository currently stores the project adapter and governance contract. When the actual Shopify theme/app source repository is connected to GitHub, place a small repo-local `AGENTS.md` there that inherits this adapter rather than duplicating the full standards.
