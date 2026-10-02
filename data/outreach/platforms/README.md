# Drag&Drop Designer Platform Registry

Source snapshot: 2026-08-10 (Google Drive master research file)
Vinterro One ingest date: 2026-10-02

## Platform source files
- Hipicon: data/outreach/platforms/hipicon-2026-10-02.csv
- Local Makers: data/outreach/platforms/local-makers-2026-10-02.csv
- Hi&Co: data/outreach/platforms/hiandco-2026-10-02.csv
- NowShopFun: data/outreach/platforms/nowshopfun-2026-10-02.csv

## Required enrichment before send
Every lead must be enriched with:
- verified business/public email
- website
- Instagram/social where available
- city/region and country
- product category
- representative products / collections
- short brand story or reason-to-contact
- relationship history
- Drag&Drop Gmail dedupe result
- bounce / opt-out status

## Mail Agent gates
`blocked_until_enriched` means NO SEND.
Only records promoted to `ready_for_personalized_outreach` may enter send queue.
Historical Hi&Co relationships must use `reactivation_review`, never cold outreach.
First cold touch must not include commission percentage or payout timing.
