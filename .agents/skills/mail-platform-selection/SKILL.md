---
name: mail-platform-selection
description: Select the correct mail architecture for transactional email, WordPress/Hostinger forms, Shopify notifications, newsletters, SMTP/API delivery, local testing or self-hosted mail. Use before adding or replacing a mail library/provider/server.
---

# Mail Platform Selection

Follow `docs/standards/MAIL_ENGINEERING.md`.

## Goal
Choose the smallest reliable mail stack for the actual job without conflating mailbox operations, templates, transport, campaigns and mail-server infrastructure.

## Inspect first
Determine:
- project/platform: Shopify, WordPress/PHP, Node/React, other backend
- mail class: human mailbox action, transactional, form/lead notification, marketing/newsletter, inbound mailbox, bulk campaign
- expected volume and latency
- current sender domain/provider and existing working transport
- required template technology and localization
- need for bounce/complaint/unsubscribe analytics
- privacy/compliance constraints
- whether durable queues/retries are needed
- whether the user truly wants to operate a mail server

## Candidate routing
- Human mailbox read/reply/send → connected Gmail/Outlook/mailbox tools, not application SMTP code.
- Shopify native order/account notification → keep Shopify-native unless a real backend/app requirement exists.
- WordPress form/transactional mail → `wp_mail()`/hooks + authenticated SMTP/API transport; no core PHPMailer edits.
- PHP standalone backend → maintained PHPMailer/Symfony-Mailer-class transport; do not hand-roll MIME/SMTP.
- React/TypeScript template source → React Email candidate.
- Provider-neutral template compiler → MJML candidate.
- Local/staging capture/integration testing → Mailpit candidate.
- Newsletter/list/segmentation/campaign management → listmonk-class system or managed campaign provider.
- High-control self-hosted application MTA → Postal-class candidate only after operations gate.
- Full self-hosted mail/collaboration server → Stalwart-class candidate only after operations/license/security gate.

## Decision output
Return:
- `current_state`
- `mail_class`
- `recommended_architecture`
- `KEEP | ADAPT | MIGRATE | SELF_HOST_JUSTIFIED | REJECT`
- `renderer/template_source`
- `transport`
- `queue/retry_need`
- `delivery_event_need`
- `testing_strategy`
- `deliverability_work`
- `security/privacy_risks`
- `migration/rollback_notes`

## Rules
- Do not add a new provider/library solely because it is popular.
- Do not self-host MTA infrastructure to solve a simple contact-form delivery problem.
- Do not migrate a working provider without measurable need.
- Do not send production lists during testing.
- Treat current provider limits/pricing/DNS requirements as runtime facts and verify upstream before implementation.
