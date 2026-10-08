---
name: sales-lead-qualification
description: Score and qualify Vinterro Digital sales-intelligence prospects using evidence-backed need, fit, reachability, confidence and account-level dedupe. Does not send.
---

# Sales Lead Qualification & Scoring

Owner: `Sales Intelligence Agent / Satış İstihbarat Ajanı`.

## Hard gates

A candidate cannot be `OUTREACH_READY` unless:
1. business identity is resolved with at least medium confidence;
2. a concrete Vinterro Digital opportunity is supported by current evidence;
3. account-level duplicate history is clear;
4. no opt-out/suppression/active-thread conflict exists;
5. the proposed contact route is public and appropriate;
6. the opportunity claim can be stated truthfully without invented metrics.

For first-touch email, Gmail/CRM/outreach account history remains authoritative. A different email never creates a fresh account.

## Score

Score 0-100 only after hard-gate review:
- Need / opportunity severity: 0-35
- Commercial / ICP fit: 0-25
- Public reachability: 0-15
- Evidence confidence/freshness: 0-15
- Locale/market fit: 0-10

Suggested tiers:
- 80-100: `A_HIGH_PRIORITY`
- 65-79: `B_QUALIFIED`
- 50-64: `C_ENRICH_OR_NURTURE`
- below 50: `LOW_PRIORITY`

A high numeric score never overrides a failed hard gate.

## Website-led campaign rule

For campaigns targeting missing/broken websites:
- website need should be one of the verified classifications from `website-opportunity-audit`;
- `NO_OWNED_SITE_FOUND`, `DOWN_OR_UNREACHABLE`, `DNS_TLS_OR_REDIRECT_FAILURE` and proven `BROKEN_RENDER_OR_CORE_FLOW` may receive high need scores;
- `COMMERCIAL_JOURNEY_WEAK` requires a concrete observed path problem;
- `UNKNOWN` cannot be described as broken and normally remains enrichment-only.

## Output states

Use one:
- `OUTREACH_READY`
- `SOCIAL_ONLY`
- `CONTACT_UNRESOLVED`
- `ENRICH_MORE`
- `DUPLICATE_BLOCKED`
- `SUPPRESSED`
- `ACTIVE_RELATIONSHIP`
- `DISQUALIFIED_NO_CLEAR_OPPORTUNITY`

Keep a human-readable reason and evidence provenance for every state.
