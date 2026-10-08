---
name: sales-intelligence-handoff
description: Convert a qualified Sales Intelligence Agent prospect into an outreach-ready evidence packet for Vinterro Digital Outreach/Mail Agent without sending or mutating campaign state.
---

# Sales Intelligence Handoff

Owner: `Sales Intelligence Agent / Satış İstihbarat Ajanı`.

## Boundary

This skill prepares a prospect packet. It does **not** send email, DM, campaign writes or autonomous follow-ups.

Handoff destination:
- cold first-touch -> `Vinterro Digital Outreach Ajanı`;
- mail render/send -> `Vinterro Digital Mail Ajanı`;
- bounce/obsolete contact -> `Contact Recovery Research Agent`;
- uncertain website evidence -> website audit / independent QA;
- non-Turkish customer-facing copy -> exact language specialist + Multilingual Localization QA Auditor.

## Required packet

Each `OUTREACH_READY` account includes:
- canonical business identity;
- region/country/city;
- business category;
- verified public website state;
- concise evidence-backed opportunity;
- official/public sources;
- public business contact + source;
- official social profile when useful;
- Gmail/CRM/account-level dedupe result;
- opt-out/bounce/reply/active-thread status;
- fit/need/reachability/evidence score components;
- total score + tier;
- recommended outreach language;
- one primary message angle;
- claims that must NOT be made;
- evidence recheck timestamp;
- account aliases/domains/emails used for dedupe.

## Handoff rule

No production first-touch send is authorized merely because a lead is `OUTREACH_READY`. The downstream outreach/mail lane must still run the canonical Vinterro Digital account-claim, Gmail-history, template, locale, MailQA and user-approval rules that apply to the requested batch.

For "web sitesi olmayan/bozuk işletmeler" campaigns, recheck the website state immediately before drafting or sending if the prior evidence is older than 24 hours.
