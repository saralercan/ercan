# Drag&Drop Platform Designer Lead Registry — Mail Agent Contract

Generated: 2026-10-02

## Scope
Sources: Hipicon, Local Makers, Hi&Co, NowShopFun.

## Hard gates
Mail Agent MUST NOT send a cold email until the record has:
- verified public/business email
- product/category description
- region or country
- source platform
- Gmail dedupe check by brand + email + domain
- no bounce suppression / no explicit opt-out
- no known historical Hi&Co relationship unless a relationship-aware reactivation path is explicitly approved

## First-touch standard
- Personalized to real product / collection / craft / material / region.
- Explain why Drag&Drop is contacting this brand.
- Position B2C + relevant B2B opportunity.
- May state there is no monthly fixed fee / listing fee.
- Do NOT state commission % or payout timing in first cold touch.
- No BCC; one-by-one send.
- From must be: Drag&Drop <info@draganddrop.tr>.
- Commercial terms are shared after interest or when directly asked.

## Enrichment fields
email, phone, website, instagram, region, country, product_category, products, brand_story, relationship_status, outreach_status, enrichment_status.

## Source registry
See: data/outreach/dragdrop-platform-designers-2026-10-02.jsonl

## Operational rule
The registry is a lead source, not an automatic send list. Records with `blocked_until_enriched` must be researched and verified before any outreach.
