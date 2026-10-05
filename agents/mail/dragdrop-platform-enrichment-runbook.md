# Drag&Drop Platform Lead Enrichment Runbook

## Goal
Turn the four platform rosters into a verified, deduplicated outreach database for Drag&Drop and Mail Agent.

## Source snapshot
- Hipicon: 2,567
- Local Makers: 267
- Hi&Co: 197
- NowShopFun: 271
- Source rows: 3,302
- Unique lead identities after normalized-name dedupe: 2,895
- Cross-platform duplicate rows collapsed: 407

## Roles
### Research / Enrichment agents
For each blocked record, collect and verify:
1. official website
2. public/business email
3. public business phone when available
4. Instagram / other relevant social profile
5. city / region / country
6. product category
7. representative products / collections
8. concise brand story / reason Drag&Drop is relevant
9. source URLs and verification date

### Relationship-history agent
Check Gmail + internal Hi&Co history before any cold outreach:
- brand name
- current and historical email
- domain
- prior Hi&Co commercial relationship
- prior Drag&Drop outreach
- opt-out / decline
- bounce history

Historical Hi&Co relationships must be tagged:
- relationship_status = known_historical_hiandco
- outreach_status = reactivation_review

### Mail Agent
May send only when:
- enrichment_status = enriched_verified
- Gmail dedupe = clear
- valid business email exists
- product/category and location exist
- no bounce suppression
- no opt-out
- no historical relationship requiring reactivation review
- outreach_status = ready_for_personalized_outreach

First touch:
- personalized from actual product/material/collection/region
- explain why Drag&Drop is contacting the brand
- B2C + relevant B2B opportunity
- state the current verified standard sales commission: **30%**
- may say no monthly fixed fee / listing fee
- do not invent or state payout timing unless a current verified written commercial rule exists for that recipient/workflow
- do not add other unverified numeric commercial terms
- no BCC; one-by-one
- sender: Drag&Drop <info@draganddrop.tr>

### Supervisor / reviewer / release gate
Before send batch:
- sample-check personalization accuracy
- reject invented product/location claims
- reject duplicates
- reject wrong sender
- reject commercial numbers in first cold touch
- verify bounce/opt-out suppression

## Priority
1. Historical Hi&Co records: enrich first but route to reactivation review, not cold send.
2. Multi-platform independent designers / studios: high confidence, enrich next.
3. Local Makers + NowShopFun independent makers.
4. Hipicon mixed directory: classify eligibility before enrichment; exclude irrelevant mass-market/global/non-design profiles.

## Important
The source roster is not an automatic send list. No record may bypass enrichment and dedupe gates.
