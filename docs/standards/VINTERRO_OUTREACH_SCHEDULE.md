# Vinterro Digital Outreach Schedule & Copy Policy

Status: active  
Version: 2.0 (2026-10-30)  
Timezone: Europe/Istanbul

This file is the canonical shared rule for **Vinterro One → Sales · AutoGTM → Vinterro Sales Super Agent** outreach scheduling and for the copy produced by the Mail and Text/Copy agents. It does not create a second campaign database, queue or CRM source of truth.

## Daily outreach slots

Run two daily first-touch outreach slots:

- **08:00 Europe/Istanbul**
- **20:00 Europe/Istanbul**

Each slot may contact **up to 30 new, distinct, verified, qualified businesses per region**. Targets are conditional on candidate quality, independent account/identity review, provider/platform permission and the mandatory per-message atomic prepare token.

Canonical 12 non-overlapping regions:

1. Türkiye
2. Yunanistan anakarası / geneli (**Sisam, Midilli, Sakız ve Kos hariç**)
3. Tiflis / Gürcistan
4. Sisam / Samos
5. Midilli / Lesvos
6. Sakız / Chios
7. İstanköy / Kos
8. Bulgaristan
9. Romanya
10. Almanya
11. Fransa
12. Dubai / Birleşik Arap Emirlikleri

Therefore:

- per slot maximum target: **360** new qualified first-touch Gmail SENT records
- daily maximum target: **720**, subject to genuine eligibility and platform permission
- 08:00 and 20:00 cohorts must contain different businesses
- an overage in one region never fills another region's quota
- previous SENT, reply, bounce, opt-out, alias/domain/account conflict, or ambiguous delivery blocks another initial contact
- failed/bounced/unresolved-delay messages do not count as successfully delivered quota units

**Keep the recurring outreach schedule in place unless the user explicitly stops it.** If sending is prohibited or the per-message permission returns `allowed=false` or lacks a valid token, continue permitted research, dedupe, copy and draft QA without sending. Never bypass provider/platform controls. Never restart the Vinterro One executor without explicit user authorization. Send only from `info@vinterro.digital`; no BCC or first-touch attachments. Customer replies require separate explicit approval.

## Shared ownership

### Mail Agent / @MailAgent
Owns:
- slot scope and quota accounting;
- Gmail history dedupe;
- sender/recipient validation;
- send execution;
- SENT verification;
- DSN/bounce/failure/delay reconciliation;
- replacement selection;
- CRM/outreach ledger updates;
- final region-by-region delivery report.

### Text Agent / @TextAgent
`metin ajanı`, `@TextAgent`, `OutreachCopywriter`, `OutreachCopyEditor`, `EmailCopywriter` and equivalent Vinterro Digital outreach-copy requests resolve to the same evidence-grounded copy contract.

The Text Agent owns:
- message brief;
- prospect-specific opening observation;
- commercially relevant opportunity framing;
- explicit web action;
- Google Ads + Meta Ads angle when genuinely relevant;
- one clear CTA;
- locale/language quality;
- natural human prose and brand tone;
- copy QA before Mail Agent execution.

The Text Agent does **not** own mailbox sending, delivery-state truth or duplicate-state truth. Those remain with Mail Agent / Outreach / Gmail / CRM.

## Pre-send account dedupe

Before every first-touch send, reconcile the account using all available canonical evidence:

- brand/business name;
- known aliases;
- domain and owned website;
- booking/store/marketplace URL;
- exact email address;
- Gmail SENT history;
- Gmail thread/reply history;
- bounce/failure/delay history;
- opt-out/unsubscribe history;
- CRM/outreach ledger.

A different email address does **not** make an already-contacted business a new prospect.

Block first-touch when:
- the business has already received cold outreach;
- a reply exists;
- an opt-out/unsubscribe/do-not-contact exists;
- the business/address has a known bounce or unresolved delivery ambiguity;
- account identity cannot be reconciled safely.

## Qualification sequence

Use:

`DISCOVER -> RAW EVIDENCE -> NORMALIZE -> DEDUPE -> VERIFY BUSINESS -> VERIFY WEBSITE/SALES CHANNEL -> VERIFY SOCIAL -> VERIFY CONTACT -> OPPORTUNITY DIAGNOSIS -> SCORE -> OUTREACH READY -> QA`

Prefer:
- independent/boutique producers;
- designers, workshops and studios;
- local brands;
- boutique food/wine/ceramics/furniture/decor businesses;
- restaurants/cafes;
- tourism and experience businesses;
- businesses dependent on social, marketplace or booking platforms;
- active businesses with no owned website where an owned conversion path is a real opportunity.

Avoid:
- mature businesses with strong owned acquisition systems and no observed material gap;
- stale/inactive businesses;
- guessed contacts;
- low-evidence leads selected only to complete a quota.

## Public contact rule

Use only verified public business contact routes from credible sources.

Never:
- invent or infer an email pattern;
- use hidden/private personal contact data;
- re-use a known bounced address;
- use a different address to bypass account-level dedupe.

If no qualified public email exists, retain the business as a social/phone lead and use another qualified business for the email quota.

## Message contract

Every first-touch message must be individually written from verified evidence.

Required:
- one concrete verified observation;
- a narrow commercial diagnosis;
- an explicit relevant web action: build, redesign, repair or improve only the necessary sections;
- Google Ads demand capture and/or Meta Ads demand generation/retargeting when genuinely relevant;
- Instagram/Facebook only as supporting layers;
- one concise CTA;
- no attachment on first touch;
- no AI jargon, generic agency filler or fabricated performance claims.

Language:
- Türkiye: natural professional Turkish;
- Greek regions: natural professional Greek;
- Tiflis / Gürcistan: professional English unless a better verified locale is explicitly selected;
- Bulgaristan: natural professional Bulgarian;
- Romanya: natural professional Romanian;
- Almanya: natural professional German;
- Fransa: natural professional French;
- Dubai / BAE: professional English, or natural Arabic where appropriate.

Use the canonical Vinterro Digital email visual shell and signature defined in:
- `docs/standards/VINTERRO_MAIL_AGENT.md`
- `docs/standards/VINTERRO_OUTREACH_CANONICAL_TEMPLATE.html` (locked, approved outreach HTML)

## Slot execution and QA

For each region and slot:

1. build a qualified candidate reserve larger than the quota;
2. run account-level dedupe immediately before send;
3. send one recipient/business at a time;
4. inspect the first real SENT message for that region/slot;
5. verify sender, body alignment, signature, personalization, explicit web action, relevant Google/Meta offer and CTA;
6. if the first-send QA is malformed or generic, stop the remaining sends for that region/slot;
7. verify each send in Gmail SENT, then record message ID, thread ID, time and raw MIME evidence;
8. reconcile new DSN/bounce/failure/delay events;
9. replace failed quota units only with a completely new qualified business from the same region;
10. do not resend to the bounced business under another email address;
11. update the canonical account/activity ledger.

## Mandatory pre-send permission

For each candidate, reconcile Gmail SENT, prior claims, bounce and opt-out at business, domain, brand, alias and all known email levels. The canonical `public.vinterro_prepare_first_touch(...)` must return `allowed=true` and a valid `send_attempt_token` for that individual message. Independently confirm sender account/alias, current provider/channel permission, and domain authentication. If any requirement fails, do not send and do not record success; research and permitted draft QA may continue. The historical release-switch convention is retired and must not be restored.

## Success accounting

Count one successful quota unit only when:
- it is a new account;
- qualification passed;
- account-level dedupe passed;
- Gmail SENT evidence exists;
- no hard bounce/failure is known;
- no unresolved delay blocks success;
- the account is not suppressed.

SENT acceptance alone is not proof of inbox placement. Report delivery truth exactly as evidenced.

## Reporting

For each slot report:
- successful new sends by region;
- businesses/emails sent;
- duplicate/previous-contact suppressions;
- opt-outs;
- bounces/failures/delays;
- replacements;
- unresolved gaps.

Do not merge quotas across regions or between the 08:00 and 20:00 cohorts.

## Authority

This policy is loaded by both the Vinterro Mail Agent and Vinterro outreach Text/Copy Agent. If a lower-level prompt, chat instruction or generated draft conflicts with this file, this canonical project rule wins unless the user explicitly changes the rule.
