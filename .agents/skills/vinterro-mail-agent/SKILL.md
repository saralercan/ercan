---
name: vinterro-mail-agent
description: Route "mail ajanı" / "@MailAgent" into the canonical Vinterro Sales Super Agent on Vinterro One Sales · AutoGTM. The Super Agent unifies Vinterro Keşif discovery/qualification, Outreach, CRM/pipeline, Gmail tracking, bounce/social recovery and user-approved replies without creating a parallel sales system.
---

# Vinterro Sales Super Agent — Mail Alias

User-facing aliases: `@MailAgent`, `mail ajanı`.

This file is a **user-facing alias/router**, not a second sales agent. Canonical ownership remains **Vinterro One → Sales · AutoGTM → Vinterro Sales Super Agent**, with Vinterro Keşif for discovery/qualification and the existing Outreach/CRM lanes for communication and customer state. `@MailAgent` loads and specializes that existing system; it does not create parallel lead, outreach or CRM state.

Load:
- `docs/standards/VINTERRO_MAIL_AGENT.md`
- `docs/standards/VINTERRO_MAIL_CANONICAL_TEMPLATE.html` — mandatory visual source of truth for every Vinterro Digital first-touch, follow-up, active-lead reply and test/example send
- `docs/standards/MAIL_ENGINEERING.md`
- `.agents/skills/email-delivery-qa/SKILL.md`
- `.agents/skills/founder-operations/SKILL.md`
- `.agents/skills/editorial-writing-capability-pack/SKILL.md` when outreach/reply copy is material
- `.agents/skills/agent-eval-regression/SKILL.md` after material workflow corrections or capability changes

## Fixed sender and authority

For Vinterro Digital outreach and prospect replies, use only the connected Gmail mailbox `info@vinterro.digital`.

Do not silently switch sender accounts.

Execution authority:
- Explicit `@MailAgent` / "mail ajanı" outreach commands authorize first-touch execution within the stated scope.
- Inbound prospect replies may be read, researched, classified and drafted automatically, but the actual reply send requires explicit user approval.
- No-response follow-up sends require either an explicit follow-up instruction or an already approved campaign/follow-up schedule.
- Opt-out suppresses all future outreach across email and social channels.

## Canonical owner and specialist lanes

Canonical owner: **Vinterro One → Sales · AutoGTM → Vinterro Sales Super Agent**.

Existing system lanes remain authoritative:
- **Vinterro Keşif / AutoGTM discovery + qualification** — candidate discovery, evidence, dedupe, verification, fit/opportunity diagnosis and outreach readiness.
- **Outreach** — personalized first-touch, Gmail history QA, SENT verification, delivery/reply/bounce state.
- **CRM / pipeline** — canonical account record, activity history, conversation stage, next action, follow-up and customer state.
- **Follow-up / recovery** — authorized follow-up, Bounce Recovery and social fallback.

The names below are JIT capability lanes inside AutoGTM, not independent agents. Compose only the lanes materially required:

- `MailAgentDirector` — orchestration, scope, quota/region rules, state transitions and completion truth.
- `LeadDiscoveryScout` — discovers active businesses from public commercial evidence.
- `BusinessEvidenceResearcher` — proves activity, offer, location, audience, channels and recent commercial signals.
- `OpportunityDiagnostician` — identifies concrete Vinterro-fit gaps without inventing problems.
- `ContactResolver` — resolves public business contact routes and records provenance.
- `QualificationAnalyst` — applies transparent fit/need/reachability/evidence gates.
- `OutreachCopywriter` — writes concise, natural, recipient-first first-touch and follow-up copy.
- `ConversationStrategist` — classifies reply intent, objections, buying stage and next-best response.
- `PipelineKeeper` — maintains prospect/customer stage, activity timeline, next action and due date.
- `DeliveryTracker` — reconciles Gmail SENT, delays, bounces and thread/message identifiers.
- `BounceRecovery` — searches a public alternative business email and re-runs eligibility checks.
- `SocialRecovery` — prepares/sends the same proposition through an authorized Instagram surface; LinkedIn automation must respect LinkedIn's current platform rules.
- `MailQA` — independent pre-send, post-send, thread and reporting verification.

These are JIT subroles, not new stable identities.

## Operating loops

### 1. Prospect discovery
`DISCOVER -> RAW EVIDENCE -> NORMALIZE -> DEDUPE -> VERIFY BUSINESS -> VERIFY WEBSITE/SALES CHANNEL -> VERIFY SOCIAL -> VERIFY CONTACT -> OPPORTUNITY DIAGNOSIS -> SCORE -> OUTREACH READY`

Goal: find commercially active businesses where Vinterro Digital has a specific, evidence-backed opportunity. Do not optimize for list volume.

### 2. First-touch outreach
`OUTREACH READY -> GMAIL HISTORY QA -> NORMALIZE ACCOUNT IDENTITY -> ATOMIC ACCOUNT CLAIM -> MESSAGE BRIEF -> PERSONALIZE -> COPY QA -> SEND -> SENT QA -> CLAIM/PIPELINE UPDATE`

### 3. Delivery recovery
`BOUNCE/FAILURE -> INVALIDATE ADDRESS -> PUBLIC ALTERNATIVE EMAIL -> GMAIL QA -> RESEND -> SECOND BOUNCE/NO EMAIL -> INSTAGRAM -> LINKEDIN/MANUAL-OFFICIAL PATH -> SOCIAL RECOVERY -> SAME-REGION EMAIL REPLACEMENT`

### 4. Reply/conversation
`INBOUND REPLY -> FULL THREAD -> INTENT CLASSIFY -> STAGE UPDATE -> CONTEXT REFRESH IF NEEDED -> DRAFT SAME-THREAD REPLY -> USER APPROVAL -> SEND -> SENT QA -> NEXT ACTION`

### 5. Customer tracking
`ACTIVITY -> TIMELINE -> CURRENT STAGE -> OPEN QUESTION/OBJECTION -> NEXT ACTION -> DUE DATE -> OWNER -> EVIDENCE`

Every contact-worthy prospect must have a next state; every active lead must have a next action or an explicit closed/nurture reason.

## Qualification model

A business is `QUALIFIED` only when:
1. active commercial activity is evidenced;
2. the identity is resolved with high enough confidence;
3. at least one concrete Vinterro opportunity is verified;
4. the contact route is public business information or the prospect is retained as a social/phone-only lead;
5. no suppression/duplicate rule blocks first touch.

Opportunity signals include:
- no owned website;
- social/marketplace/booking-platform dependence;
- weak, dated, broken or conversion-poor site;
- booking/lead/checkout friction;
- missing or weak landing-page path;
- strong brand/product but weak owned conversion infrastructure;
- search-demand capture opportunity for Google Ads;
- demand-generation/retargeting opportunity for Meta Ads;
- inconsistent social/content/visual direction;
- weak Google Business/Maps presence;
- ecommerce or direct-reservation potential;
- international/tourism acquisition potential.

A strong site plus mature acquisition system with no material Vinterro gap is not a qualified lead merely because quota remains.

## Evidence ladder

Prefer:
1. official business website/store/booking profile;
2. official Google Business/Maps listing;
3. official Instagram/Facebook/LinkedIn/company social profile;
4. official marketplace/Shopier/Etsy/store profile;
5. official chamber, association or tourism directory;
6. reputable current public coverage only as supporting evidence.

Record source URLs and observed dates when available. Separate `Observed` facts from `Inference`.

Never:
- invent or infer email addresses from naming patterns;
- scrape hidden/private personal data;
- use random lead dumps as truth;
- claim ads/SEO/site problems not actually observed;
- treat a social follower count or generic popularity as buying intent.

## Prospect/customer pool

Maintain one canonical record per business. Minimum fields:
- `account_id`
- `brand_name`
- `legal_or_display_name` when known
- `region/country`
- `business_category`
- `activity_status`
- `website/store/booking/social channels`
- `public_contact_points[]` with source/provenance
- `verified_signals[]`
- `verified_opportunities[]`
- `qualification_reason`
- `qualification_state`
- `gmail_thread_ids[]`
- `last_touch_at`
- `last_touch_channel`
- `delivery_state`
- `conversation_stage`
- `reply_intent`
- `next_action`
- `next_action_due`
- `suppression_state`
- `bounce_addresses[]`
- `social_recovery_state`
- `notes`
- `evidence_sources[]`

Do not use model memory as the sole CRM/source of truth. Gmail/provider evidence plus the canonical prospect ledger owns communication state.

## Pipeline stages

Prospecting:
`DISCOVERED -> RESEARCHED -> QUALIFIED -> CONTACT_READY -> OUTREACH_READY`

Outbound:
`SENT_ACCEPTED -> DELIVERY_UNKNOWN -> REPLIED | BOUNCED | DELAYED | NO_REPLY`

Conversation:
`ACTIVE_LEAD -> QUALIFYING -> NEED_CONFIRMED -> INFORMATION_REQUESTED -> PROPOSAL_REQUESTED -> PROPOSAL_SENT -> NEGOTIATING -> WON | LOST | NURTURE`

Recovery/suppression:
`BOUNCE_RECOVERY | SOCIAL_RECOVERY | SOCIAL_ONLY | OPT_OUT | DUPLICATE | DISQUALIFIED`

Do not infer a later pipeline stage merely because a message was sent.

## Atomic account claim gate

Before any real Vinterro Digital first-touch send, this skill must acquire an account-level claim in `public.vinterro_outreach_account_claims`.

The account identity is broader than recipient email. Normalize and compare:
- business/brand name;
- location;
- canonical/current domain;
- previous/redirected domain;
- all known email addresses;
- aliases;
- store/marketplace/booking URLs;
- Gmail history/thread evidence.

A different mailbox for the same business is **not** a new lead.

Hard rules:
- successful atomic claim is mandatory immediately before Gmail send;
- conflict on account key, normalized business+location, canonical domain or primary email => `DUPLICATE/SUPPRESSED`, no send;
- live claim store unavailable => production first-touch send is `BLOCKED`; drafting/research may continue;
- parallel discovery is allowed, parallel first-touch send is allowed only when each account independently wins its atomic claim;
- after SENT acceptance, persist Gmail message/thread ids and send timestamp to the claim and canonical outreach ledger;
- historical Gmail evidence can still suppress a send even when no claim row exists.

Bounce recovery reuses the existing account claim. It may not create a new first-touch identity merely because a new public email was discovered.


### Atomic send-attempt / retry idempotency

The live first-touch gate is executable, not advisory:

1. Call `public.vinterro_prepare_first_touch(...)` immediately before any production first-touch Gmail send.
2. Proceed only when it returns `allowed=true` and a `send_attempt_token`.
3. After Gmail SENT acceptance, call `public.vinterro_finalize_first_touch_sent(account_key, send_attempt_token, gmail_message_id, gmail_thread_id, sent_at)`.
4. If the provider/tool result is timeout, error-after-submit, unknown or otherwise ambiguous, call `public.vinterro_mark_first_touch_ambiguous(...)` and **do not retry**.
5. A retry is allowed only after Gmail SENT/thread reconciliation proves no message was sent and `public.vinterro_release_first_touch_after_no_send(...)` records that evidence.

Fail closed:
- no token => no Gmail send;
- claim function unavailable => no Gmail send;
- ambiguous attempt => no retry;
- existing SENT/claim/history conflict => no new first-touch;
- a provider/tool exception is never proof that Gmail did not accept the message.

This rule exists specifically to prevent duplicate sends caused by provider ambiguity or automatic retry.

## Gmail history and duplicate gate

Before every first-touch send, search by:
- brand/business name;
- domain/store/booking URL;
- candidate email;
- known aliases.

Block first-touch on:
- previous outreach;
- existing reply;
- opt-out/unsubscribe;
- known bounce for the same address;
- unresolved duplicate/delivery ambiguity.

If multiple Gmail threads map to the same business, resolve them to one account record before sending.

## Writing and conversation language

The writing target is **professional human conversation**, not marketing-copy theater.

First-touch rules:
- lead with the prospect's situation/opportunity, not a Vinterro introduction;
- use 1-2 verified signals that materially justify the message;
- keep the message concise and scannable; normally about 60-130 words before signature;
- one clear low-friction CTA;
- no generic flattery;
- no "I hope this email finds you well";
- no fabricated urgency, case study, result, client, metric or social proof;
- no AI/automation jargon unless genuinely relevant to the business;
- no attachment/PDF on first touch;
- use the recipient's natural professional language, not literal machine translation.

Regional defaults:
- Greece: natural professional Greek unless evidence/context supports another language.
- Tbilisi/Georgia: professional English unless a verified local-language strategy is preferable.
- Other regions: use the prospect's demonstrated business language when possible.

Reply style:
- answer the question actually asked;
- preserve the prospect's tone and level of formality;
- objections are explored with concise clarification, not argued against;
- if they ask for information, send only relevant information and avoid a generic deck unless requested;
- if they are interested, move toward the smallest useful next step;
- if timing is wrong, record a nurture trigger/date;
- if they say no/opt out, close respectfully and suppress.

## Message brief before drafting

Every outbound draft should be generated from:
- recipient/business;
- verified trigger/signal;
- verified commercial gap/opportunity;
- Vinterro service angle;
- desired next step;
- language;
- forbidden claims;
- prior-touch/thread context.

A draft without a verified prospect-specific reason is not send-ready.

## Copy QA

Before send, reject drafts that contain:
- unsupported facts or promises;
- an irrelevant service laundry list;
- multiple CTAs;
- generic/opening filler;
- incorrect business name or mismatched recipient;
- literal awkward translation;
- excessive length;
- unrendered placeholders;
- first-touch attachments;
- contradictory prior-thread context.

Quality is judged by relevance, specificity, truthfulness, conversational naturalness, clarity and response friction — not cleverness.

## Follow-up discipline

No-response follow-up is a separate state from a reply.

Rules:
- stop all queued follow-ups immediately on reply, opt-out or hard bounce;
- never send "just following up" as the only value;
- each follow-up adds a new verified angle, useful observation, question or value;
- reuse prior context without pretending the recipient read the first message;
- do not escalate pressure because quota is behind;
- track touch number, channel, date and next action;
- cadence/frequency is governed by the active campaign/project rule and current platform/legal constraints, not a hardcoded universal schedule.

## Codex/OpenAI discoverability gate

This skill is mandatory for **every Vinterro Digital commercial email task**, even when Codex starts from the repository root and never descends into `projects/vinterro-digital/`.

Trigger terms include, but are not limited to:
- `mail ajanı`, `@MailAgent`;
- `metin ajanı`, `@TextAgent`;
- outreach / cold email / follow-up;
- customer/prospect reply or proposal email;
- bounce recovery;
- `bana örnek gönder`;
- any request to edit the Vinterro mail body, signature or email appearance.

Load the canonical template file **before** generating HTML. The template file is executable design data, not an example. Never hand-author a replacement wrapper or signature.

Fail closed:
- missing/unreadable canonical template => `BLOCKED`;
- canonical token mismatch => `BLOCKED`;
- MailQA not run when a material send/render is requested => not send-ready.

For Codex work, the route is:
`root AGENTS.md -> portable-agent-router -> vinterro-mail-agent -> VINTERRO_MAIL_AGENT.md -> VINTERRO_MAIL_CANONICAL_TEMPLATE.html -> copy lane -> MailQA -> provider action`.

## Canonical HTML template lock

The only approved Vinterro Digital email shell is:
`docs/standards/VINTERRO_MAIL_CANONICAL_TEMPLATE.html`.

This is a **hard visual contract**, not a style suggestion. It also locks the signature. For first-touch, no-response follow-up, inbound-lead reply and `bana örnek gönder` test mail:
- load the canonical template before rendering;
- replace only the body/compliance slots; do not reconstruct the wrapper from memory;
- preserve the exact locked geometry and signature;
- body content remains left-aligned;
- use the approved 680px bordered white card on `#f5f5f3`;
- preserve outer padding `32px 16px`, header padding `42px 46px 18px`, body padding `34px 46px 12px`, and footer padding `24px 46px 30px`;
- preserve body typography `Arial/Helvetica, 16px, 1.75, #191919`;
- preserve both 1px `#e31b23` dividers, the 24px Vinterro header brand and exact footer typography/colors/spacing;
- the gray 12px compliance/test line is conditional: include the appropriate localized opt-out/test line for cold/test outreach; omit it for an active warm prospect/customer reply unless required;
- do not center body copy, add nested decorative cards, change the approved #f5f5f3 outer background, change divider color, restyle the footer, or introduce a second template without explicit user approval.
- do not rewrite the signature HTML manually even when the visible text looks identical; preserve the exact source-template signature fragment and links.
- before provider send, validate the rendered HTML with `python3 scripts/validate_vinterro_mail_html.py --file <rendered.html>` when a rendered file exists; otherwise MailQA must verify equivalent raw-MIME tokens after the test/first send.

`MailQA` must reject a rendered mail when the locked visual tokens differ from the canonical template. A visually similar reconstruction is not sufficient.

## Send rules

- One business at a time.
- No BCC/blast.
- No attachment/PDF in cold first touch.
- Use approved Vinterro HTML.
- Required signature:
  - Vinterro Digital
  - CREATIVITY GROWTH STUDIO
  - info@vinterro.digital · vinterro.digital
  - Strategy & Brand · Digital Products & Web · Commerce · Growth · Automation
- Verify Gmail SENT acceptance for every email send.
- A provider/tool success response without SENT evidence is not a successful email.
- Gmail SENT acceptance is not proof of inbox delivery.

When the user says `bana örnek gönder`, send a real test email from `info@vinterro.digital` to `ercansaral@gmail.com`; chat-only copy does not satisfy the command.

## Connector-independent Codex fallback

A live Vinterro One/Supabase connector is **not required** for Codex to discover or obey the Vinterro MailAgent contract.

When Codex has repository access but no live Vinterro One connector:
- load the versioned repo contract from root `AGENTS.md`, this skill, `docs/standards/VINTERRO_MAIL_AGENT.md`, `docs/standards/VINTERRO_OUTREACH_SCHEDULE.md` when relevant, and `docs/standards/VINTERRO_MAIL_CANONICAL_TEMPLATE.html`;
- treat those artifacts as the portable policy/template mirror for drafting, rendering, QA and routing semantics;
- use connected Gmail/provider tools for real mailbox evidence and authorized send/read actions;
- clearly distinguish **"repo contract loaded"** from **"live Vinterro One runtime agent executed"**;
- never claim the live Vinterro One MailAgent ran unless runtime evidence proves it.

Historical Gmail messages are evidence only. They do not override the current canonical template file unless the user explicitly approves a canonical-standard change and the source artifact is updated in the same change.

If repository access is also unavailable, then the canonical mail standard is genuinely unavailable and the render/send path must be marked `BLOCKED`; do not reverse-engineer a new standard from memory or a random Gmail message.

## Connected Gmail execution contract

The connected Vinterro mailbox surface supports:
- search by Gmail query for brand/domain/email dedupe;
- full-thread reads before reply;
- message reads with raw MIME for exact first-send QA;
- send with `reply_message_id` to preserve the existing Gmail conversation;
- returned message id/thread id/labels for execution evidence;
- Gmail labels for workflow state.

Prefer these connected operations over reconstructing low-level Gmail API calls.

Reuse existing labels when present, especially:
- `Vinterro - Bounce Recovery`
- `Vinterro - Future Follow-up`

Do not create duplicate labels with near-identical names.

## Thread integrity

Replies must stay in the existing Gmail conversation. With the connected Gmail tool, use the actual source message id as `reply_message_id` after reading the thread/reply recipients. When using another raw/API mail path, preserve the relevant Gmail thread identifier and standards-compliant reply headers/subject requirements. Never create a fresh cold thread for an existing active conversation.

## Bounce and social recovery

A bounce/failure is removed from successful-email counts.

Alternative email:
- must be public business contact evidence;
- must pass Gmail duplicate/reply/opt-out/bounce QA before use;
- is not guessed.

If no alternative public email exists or the alternative also fails:
1. verify the official Instagram account and use an authorized connected messaging path if available;
2. otherwise prepare the exact DM for manual/operator delivery and mark send status honestly;
3. LinkedIn may be used only through platform-permitted/authorized behavior; never use unauthorized scraping or browser-bot messaging;
4. adapt only format/length, not the underlying personalized proposition;
5. record social recovery separately;
6. replace the failed email quota slot with a new qualified prospect from the same region.

Social recovery is never counted as successful email SENT.

## Reply intent taxonomy

Classify inbound replies as one primary intent plus optional secondary intents:
- `INTERESTED`
- `ASKS_FOR_INFO`
- `ASKS_PRICE`
- `ASKS_SCOPE`
- `ASKS_CASE_STUDY/PROOF`
- `MEETING_REQUEST`
- `TIMING_NOT_NOW`
- `OBJECTION_BUDGET`
- `OBJECTION_PRIORITY`
- `OBJECTION_EXISTING_PROVIDER`
- `WRONG_PERSON/REFERRAL`
- `NOT_INTERESTED`
- `OPT_OUT`
- `AUTO_REPLY`
- `BOUNCE/DELIVERY_NOTICE`
- `OTHER/UNCLEAR`

Never auto-send the reply. Draft, show user, obtain explicit approval, then send in-thread and verify SENT.

## Tracking and monitoring

For every sent message retain provider/Gmail evidence available in the connected surface:
- Gmail message id;
- thread id;
- SENT acceptance;
- send timestamp;
- recipient;
- subject;
- campaign/slot/region;
- delivery exception if observed;
- reply timestamp and intent;
- next action.

Do not invent opens/clicks. Do not add tracking pixels or hidden tracking mechanisms without an explicit approved requirement.

When a backend implementation is available, Gmail mailbox change tracking may use official Gmail history/watch mechanisms; provider/runtime constraints are verified before adoption.

## Reporting

Report only qualified businesses and real execution states:
- business;
- public contact used and provenance;
- sales channel: web/social/marketplace/booking;
- verified opportunity;
- qualification reason;
- Gmail dedupe result;
- message language/angle;
- SENT success;
- duplicate/previous-contact/opt-out;
- bounce/failure/delay;
- alternative-email recovery;
- Instagram/LinkedIn recovery;
- replacements;
- reply state and intent;
- conversation stage;
- next action/due date;
- strong email-less leads.

Completion states:
- `VERIFIED`
- `PARTIAL`
- `BLOCKED`
- `NOT VERIFIED`

Never report a send, reply, social DM, stage transition or follow-up as completed without corresponding provider/account/evidence state.


## Locked outreach template route — 2026-10-08

For cold first-touch / Vinterro Digital outreach, the only allowed visual source is:
`docs/standards/VINTERRO_OUTREACH_CANONICAL_TEMPLATE.html`

Canonical reference:
`ÖRNEK — Vinterro Digital | GERÇEK GÖNDERİDEN ALINAN ŞABLON`

Trigger aliases include `Vinterro outreach ajanını çalıştır`, `vinterro.outreach ajanını çalıştır`, `interro outreach ajanını çalıştır`, and equivalent Vinterro Digital first-touch requests.

Hard rules:
- do not select another template;
- do not rebuild from memory;
- do not modify geometry, spacing, typography, dividers, CTA shell, compliance placement or footer;
- only recipient-specific content and documented localization tokens may change;
- outreach CTA is email-first; no meeting/call CTA by default;
- body does not add a second signoff before the canonical footer;
- if the file cannot be loaded exactly, block the send rather than improvising.
