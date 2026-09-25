# Vinterro Mail Agent Specialist Scan — 2026-09-25

## Goal

Research current open-source and official-source patterns that materially improve Vinterro Digital `@MailAgent` in:
- prospect discovery;
- lead qualification;
- personalized outreach copy;
- natural conversation/reply handling;
- customer/prospect pool creation;
- email tracking;
- bounce recovery;
- follow-up discipline;
- customer pipeline/activity tracking;
- human approval and auditability.

This scan adopts concepts, not external agent identities. Ercan OS standards, user rules and provider policies remain authoritative.

## Sources reviewed

### 1. ethanplusai/harvey — MIT
Useful patterns:
- staged prospecting pipeline;
- evidence/signals before cohort creation;
- separate sender/handler/analyst responsibilities;
- stop-on-reply;
- deterministic pre-send gates;
- conversation-stage state machine;
- one-message-at-a-time review;
- bounce invalidation + queue cancellation;
- pipeline analytics.

Decision: **ADOPT_PATTERN_ONLY**.

Reason: the state-machine, stop-on-reply and deterministic QA patterns fit Ercan OS. Do not copy its autonomous-send posture or provider-specific implementation assumptions.

### 2. eracle/OpenOutreach — GPLv3
Useful patterns:
- lead qualification produces a human-readable `reason`;
- email-less qualified leads remain valuable;
- discovery/send states are explicit;
- dedupe warning is treated as operationally important;
- qualification reason is more useful than an opaque score.

Decision: **ADOPT_PATTERN_ONLY**.

Reason: the explainable-reason pattern fits Vinterro; code/license/provider architecture is not adopted.

### 3. Nuraveda-Labs/ai-sales-agent — MIT
Useful patterns:
- discovery -> enrichment -> draft -> approval -> send;
- replies, bounces and unsubscribes route back to the lead record;
- approval and audit trail as first-class operations.

Decision: **ADOPT_PATTERN_ONLY**.

Reason: strong pattern for lead-state reconciliation and consequential action approval.

### 4. gtmagents/gtm-agents — cold-email-personalization skill
Useful patterns:
- research signals before drafting;
- personalization comes from verified research;
- short first touch;
- one CTA;
- copy QA before send;
- follow-ups rotate value rather than repeat the same ask.

Decision: **ADOPT_PATTERN_ONLY**.

Ercan OS override:
- no fixed universal score threshold;
- no requirement for a specific number/recency of signals when the business context does not justify it;
- truth and fit outrank formula compliance.

### 5. gtm-skills/gtm — MIT
Useful patterns:
- role-separated SDR/AE/RevOps workflows;
- signal-based targeting;
- tone choice based on audience;
- end-to-end research/outreach/CRM framing.

Decision: **ADOPT_PATTERN_ONLY**.

Reason: useful capability taxonomy; Ercan OS already has its own routing/approval architecture.

### 6. msitarzewski/agency-agents — Sales Outreach
Useful patterns:
- consultative, recipient-first writing;
- research before outreach;
- concise copy;
- one CTA;
- track every touch and next action;
- objection handling through clarification rather than pressure;
- disqualify poor-fit accounts.

Decision: **ADOPT_PATTERN_ONLY**.

Reason: writing and pipeline principles are useful; promotional persona claims and rigid canned cadences are not adopted.

### 7. twentyhq/twenty — open-source CRM
Useful patterns:
- configurable objects/fields/relationships;
- pipeline views;
- email/calendar sync;
- workflows;
- AI agents operating within permissions;
- duplicate detection;
- audit logs.

Decision: **REFERENCE / FUTURE CRM ADAPTER**.

Reason: strong model for a future durable MailAgent CRM surface. Not required as a new dependency for the current JIT agent.

### 8. charbelkassab/relatio-crm
Useful patterns:
- simple prospect record;
- activity timeline;
- follow-up reminders;
- mailbox thread association;
- explicit "who needs a reply?" workflow;
- AI-accessible CRM actions.

Decision: **ADOPT_PATTERN_ONLY**.

Reason: activity timeline + next-action discipline is directly useful without adopting the implementation.

### 9. OpenAI ChatGPT Sales skill: enrich-company-and-contact-data
Useful patterns:
- hard-filter verification before qualification;
- separate sourced facts from inference;
- provider/public-evidence provenance;
- never invent missing contact fields;
- preserve unresolved/near-match states.

Decision: **ADOPT_POLICY_PATTERN**.

Ercan OS override:
- Vinterro may use narrow public business research according to the user-approved workflow;
- no credit-consuming enrichment or personal-contact access is implied by this skill.

## Official platform sources

### Gmail API — Google
Adopt:
- Gmail `threads` as conversation context;
- same-thread replies preserve `threadId`, matching subject and RFC-compliant `References` / `In-Reply-To`;
- `messages.send` success is a message-send response, not proof of inbox placement;
- `users.history.list` can reconcile mailbox changes;
- `users.watch` + Pub/Sub can notify a backend of mailbox changes;
- watch expiration and delayed/dropped-notification fallback must be handled.

Decision: **ADOPT** as the canonical provider behavior when a backend/API implementation is built.

### LinkedIn official Help/User Agreement
Observed:
- LinkedIn prohibits unauthorized third-party scraping, browser bots and automated messaging/activity.

Decision: **HARD GUARDRAIL**.

Ercan OS behavior:
- research only from permitted/public evidence;
- no unauthorized browser-bot LinkedIn messages;
- send via an official/permitted integration if one exists and is authorized;
- otherwise prepare a manual/operator message and mark the send as not executed.

## Architecture adopted into @MailAgent

### Specialist lanes
- MailAgentDirector
- LeadDiscoveryScout
- BusinessEvidenceResearcher
- OpportunityDiagnostician
- ContactResolver
- QualificationAnalyst
- OutreachCopywriter
- ConversationStrategist
- PipelineKeeper
- DeliveryTracker
- BounceRecovery
- SocialRecovery
- MailQA

### Customer/prospect data model
One account record owns:
- business identity;
- channel URLs;
- public contacts with provenance;
- verified signals;
- verified opportunities;
- qualification reason;
- Gmail message/thread ids;
- activity timeline;
- delivery state;
- conversation stage;
- reply intent;
- next action/due date;
- bounce/suppression state;
- social recovery;
- source evidence.

### State machine
Prospecting:
`DISCOVERED -> RESEARCHED -> QUALIFIED -> CONTACT_READY -> OUTREACH_READY`

Delivery:
`SENT_ACCEPTED -> DELIVERY_UNKNOWN -> REPLIED | BOUNCED | DELAYED | NO_REPLY`

Conversation:
`ACTIVE_LEAD -> QUALIFYING -> NEED_CONFIRMED -> INFORMATION_REQUESTED -> PROPOSAL_REQUESTED -> PROPOSAL_SENT -> NEGOTIATING -> WON | LOST | NURTURE`

Recovery:
`BOUNCE_RECOVERY | SOCIAL_RECOVERY | SOCIAL_ONLY | OPT_OUT | DUPLICATE | DISQUALIFIED`

## Copy principles adopted

1. Research is the basis of personalization.
2. First touch starts from the prospect's situation, not a Vinterro biography.
3. Use only verified claims.
4. Prefer one commercial angle and one CTA.
5. Keep cold email concise and scannable.
6. Follow-ups add new value; they do not merely repeat "following up".
7. Replies answer the actual question first.
8. Objections are clarified, not argued with.
9. Do not fabricate case studies, results, clients, metrics or urgency.
10. Native professional phrasing outranks literal translation.

## Explicit rejections

Do not adopt:
- guessed email generators;
- hidden/private contact scraping;
- bulk list blasting;
- automatic "approve all" as the default review pattern;
- unauthorized LinkedIn automation;
- fixed universal outreach cadence;
- tracking pixels by default;
- provider acceptance as proof of delivery;
- model memory as the only CRM;
- one opaque lead score as the reason to contact;
- quota pressure as a reason to lower qualification standards.

## Result

The Vinterro Mail Agent should operate as a lightweight agentic CRM/BDR system with evidence-first discovery, explainable qualification, natural personalized copy, thread-aware conversation handling, delivery reconciliation, bounce/social recovery and explicit next-action discipline.
