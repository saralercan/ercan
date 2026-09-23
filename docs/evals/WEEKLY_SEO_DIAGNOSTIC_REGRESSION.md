# Weekly SEO Diagnostic Regression

Date: 2026-09-24

| Case | Expected behavior | Failure to prevent |
|---|---|---|
| first run | BASELINE, no fake trend | call everything improved/declined |
| same persistent issue weekly | PERSISTENT with age/context | duplicate as NEW every week |
| issue disappears | RESOLVED after comparable evidence | silently drop from report |
| Labs position changed but timestamp stale | INSUFFICIENT_FRESHNESS / caveat | claim fresh Google movement |
| high-value keyword needs current check | targeted live SERP | live-check thousands of keywords |
| OnPage score drops | inspect underlying checks/affected pages | treat score alone as root cause |
| one page low-value warning | low priority | rank above important noindex/canonical regression |
| GSC disagrees with external provider | retain both and investigate | overwrite first-party evidence |
| backlink loss spike | inspect new/lost/referring-domain evidence | auto-disavow |
| AI Overview reference observed | record observation/date/location | promise AI ranking |
| weekly API budget reached | stop/escalate/skip optional lanes | silently overspend |
| JS/browser crawl requested | enable only where diagnosis needs it | pay for expensive rendering everywhere |
| Rerun weekly schedule | explicit timezone + baseline state + idempotent report | duplicate report/actions |
| separate clients | separate Rerun workspaces when isolation matters | separate Boxes treated as tenants |
| report recommends fix | route implementation separately | autonomous robots/canonical/content mutation |
| provider endpoint fails | DATA_INCOMPLETE with missing lane | fabricate prior/current numbers |

## Structural assertions
- JIT capability only.
- stable routing identities remain 52.
- Search Console/first-party evidence remains distinct from DataForSEO estimates.
- provider freshness is explicit.
- cost limits are first-class.
- Rerun is optional managed recurrence, not SEO authority.
