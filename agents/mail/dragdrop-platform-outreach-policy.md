# Drag&Drop Platform Designer Lead Registry — Mail Agent Contract

Generated: 2026-10-02

## Scope
Sources: Hipicon, Local Makers, Hi&Co, NowShopFun.

Canonical first-touch skill: `.agents/skills/dragdrop-outreach-intro/SKILL.md`
Owner agent: `Drag&Drop Outreach Ajanı`

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
- Never use unsupported prior-contact language such as “yeniden inceledik” or “uzun süredir takip ediyoruz”.
- Write in a natural, agency-grade brand-partnerships/designer-relations voice; generic AI/template phrasing is rejected.
- Explain why Drag&Drop is contacting this brand.
- Position B2C + relevant B2B opportunity.
- State that Drag&Drop is Türkiye-based but sells internationally, with an explicit emphasis on active European sales and suitable Europe-internal / Türkiye-Europe / wider international routes.
- State the current verified standard sales commission: **30%**.
- State there is no monthly fixed fee / listing fee.
- Do NOT invent or state payout timing unless a current verified written commercial rule exists for that recipient/workflow.
- Do not add other unverified numeric commercial terms.
- No BCC; one-by-one send.
- From must be: Drag&Drop <info@draganddrop.tr>.
- The verified 30% commission and no-fixed/no-listing-fee model may be stated in first touch; any additional commercial detail is shared only when verified and relevant.

## Enrichment fields
email, phone, website, instagram, region, country, product_category, products, brand_story, relationship_status, outreach_status, enrichment_status.

## Source registry
See: data/outreach/dragdrop-platform-designers-2026-10-02.jsonl

## Operational rule
The registry is a lead source, not an automatic send list. Records with `blocked_until_enriched` must be researched and verified before any outreach.
