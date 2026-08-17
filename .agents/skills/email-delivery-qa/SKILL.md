---
name: email-delivery-qa
description: Verify application email delivery, templates, recipients, retry/idempotency, links, deliverability configuration and non-production safety. Use after material email/form/notification/newsletter changes.
---

# Email Delivery QA

Follow `docs/standards/MAIL_ENGINEERING.md`.

## Evidence required
Capture what can actually be verified:
- triggering event/input
- expected recipient/sender/reply-to
- template id/version/locale
- queue/job/message/provider ids when available
- captured/rendered HTML + plain text
- local/staging capture evidence or safe test-recipient evidence
- actual provider/transport response
- delivery/bounce/unsubscribe event evidence when relevant

## QA sequence
1. Trigger the real representative event in a safe environment.
2. Verify exactly one expected mail job/message for idempotent flows.
3. Confirm recipient, From, Reply-To, subject and preheader.
4. Inspect HTML and plain text.
5. Check dynamic data, missing-field fallbacks and escaping.
6. Verify all CTA/image/unsubscribe/preferences URLs and environment hostnames.
7. Check mobile/desktop rendering and high-risk email-client compatibility.
8. Verify no debug data, secrets, staging URLs or unintended recipients.
9. Exercise a representative transient failure/retry path when material.
10. For provider webhooks, verify authenticity check, deduplication and state transition.
11. For marketing, verify unsubscribe/suppression behavior.
12. For sender/domain changes, verify current SPF/DKIM/DMARC/provider-domain status.

## Failure severity
- **P0**: wrong recipient, duplicate customer send, secret/PII leak, spoofed sender, production-list send from staging, broken required unsubscribe, false user confirmation when lead is lost.
- **P1**: persistent delivery failure, broken CTA, incorrect locale/data, no retry for transient critical mail, bounce/suppression ignored.
- **P2**: visual/client compatibility issues that do not block message meaning, non-critical spacing/dark-mode differences.

## Result
Return one of:
- `VERIFIED`
- `PARTIAL`
- `BLOCKED`
- `NOT VERIFIED`

Never claim inbox delivery merely because the application or provider accepted the message.
