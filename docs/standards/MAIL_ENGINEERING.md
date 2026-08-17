# Mail Engineering Standard

Applies to application email, transactional notifications, contact/lead forms, newsletters, bulk campaigns, SMTP/API delivery, email templates, deliverability and mail QA across Ercan OS projects.

## Core architecture
Email is not one concern. Keep these layers explicit:
1. **Mailbox/user operations** — reading, drafting, replying, forwarding or sending from a human mailbox through Gmail/Outlook connectors or the user's approved mail provider.
2. **Application events** — order/contact/form/account/lead/business events that may trigger mail.
3. **Mail job/queue** — durable send intent with idempotency key, recipient, template/version, locale, correlation/task id and retry state.
4. **Renderer/template** — deterministic HTML + plain-text output.
5. **Transport adapter** — SMTP or provider API.
6. **Delivery provider/MTA** — managed provider by default unless self-hosting is an explicit architectural decision.
7. **Delivery events** — accepted/delivered/deferred/bounced/complained/unsubscribed/suppressed via verified webhooks where supported.
8. **Status/audit store** — minimum necessary metadata for troubleshooting and user-visible status; avoid unnecessary message-content/PII retention.

Do not collapse template, transport, mailing-list management and mail-server operations into one opaque plugin.

## Provider-selection rule
Choose the smallest operational surface that meets the requirement.
- **Managed transactional provider/API or authenticated SMTP**: default candidate for production application mail.
- **Platform-native mail**: prefer Shopify native notifications for Shopify-owned transactional flows unless an app/backend requirement materially exceeds them.
- **WordPress**: preserve `wp_mail()`/WordPress hooks and PHPMailer-based transport semantics; configure a reliable authenticated SMTP/API integration rather than raw PHP `mail()` or core edits.
- **Newsletter/list manager**: separate system when subscriptions, segmentation, campaigns, opt-outs, lists and analytics are first-class requirements.
- **Self-hosted MTA/mail server**: only when data/control/cost/scale/compliance requirements justify DNS reputation, queue, abuse, monitoring, upgrades and deliverability operations.

Never self-host a mail server just because an open-source repo exists.

## Canonical upstream patterns
Verify current status/license/docs at runtime before adoption.
- `PHPMailer/PHPMailer` — mature PHP SMTP/message construction reference; WordPress itself uses PHPMailer. Use current WordPress APIs rather than replacing bundled internals.
- `resend/react-email` — provider-neutral React/TypeScript component approach for deterministic responsive HTML/plain-text email templates.
- `mjmlio/mjml` — provider-neutral responsive-email markup/compiler; useful when React is not the desired template source.
- `axllent/mailpit` — preferred local/staging SMTP capture and email integration-test candidate. MailHog is legacy/no longer actively maintained according to Mailpit upstream.
- `knadh/listmonk` — self-hosted newsletter/mailing-list manager reference; AGPLv3, so license/operations must be considered before deployment.
- `postalserver/postal` — self-hosted application mail-server/MTA reference; not a default dependency.
- `stalwartlabs/stalwart` — modern full mail/collaboration server reference with SMTP/IMAP/JMAP and deliverability/security features; substantial operations/license implications, not a default dependency.

## Transactional vs marketing separation
Transactional and marketing mail have different contracts.

**Transactional**
- Triggered by a real user/business event.
- Delivery reliability, latency, deduplication, locale and event correctness dominate.
- Do not silently add promotional content that changes legal/consent classification.

**Marketing/campaign**
- Requires explicit audience/list/consent rules.
- Unsubscribe/suppression handling is mandatory where applicable.
- Campaign scheduling, segmentation, frequency and reporting belong in a campaign/list system, not ad-hoc loops in a web request.

Do not send a large mailing list by looping over recipients synchronously in a WordPress page request or Shopify storefront request.

## Event-to-mail contract
Every material application email should define:
- event/trigger
- recipient source and validation
- sender/from/reply-to identity
- template id + version + locale
- required data contract
- idempotency/deduplication key
- priority/TTL when relevant
- transport/provider
- retry classification
- expected delivery-event handling
- privacy/retention policy

Do not reconstruct critical email payloads later from mutable page state when the triggering transaction needs an immutable snapshot.

## Idempotency and duplicate prevention
- Assign a stable send id/idempotency key for event-driven mail.
- Retries must not create duplicate customer emails.
- Webhook events also need event-id deduplication where providers can redeliver.
- Before retrying uncertain sends, reconcile provider/message status when possible.
- Bulk/campaign systems maintain per-recipient send state rather than assuming one campaign-level success means every recipient was delivered.

## Retry policy
Classify failures before retry:
- transient network/provider 5xx/rate-limit/deferred → exponential backoff with bounded attempts;
- invalid recipient/permanent bounce/rejected policy → no blind retry; suppress or flag;
- auth/config/domain failure → stop and alert rather than hammering provider;
- uncertain response after write → reconcile by provider/message id or idempotency key.

Retry logic belongs in a durable queue/job layer for important flows, not recursive controller code.

## Deliverability and sender identity
Production sender setup must be treated as infrastructure, not copywriting.
- Authenticate the sending domain using current provider guidance and current DNS standards.
- SPF/DKIM/DMARC alignment and From/Return-Path behavior are verified for the actual provider/domain combination.
- Sender name/address/reply-to must represent the correct project/brand.
- Bounces, complaints and suppressions are consumed and reflected in send eligibility.
- Marketing mail includes current required unsubscribe mechanisms and honors opt-outs.
- Do not rotate domains/addresses or evade provider/recipient protections to push unwanted mail.

DNS records, provider verification requirements and bulk-sender rules are volatile runtime facts; verify them from current provider/mailbox-provider documentation.

## WordPress / Hostinger mail
- Use WordPress APIs/hooks; never edit core PHPMailer files.
- Prefer `wp_mail()` plus a supported transport integration or a bounded custom plugin adapter.
- Validate/sanitize form input, verify nonce/capability where relevant, rate-limit abusive public forms and prevent header injection.
- Form success UI must not claim "sent" merely because local PHP code ran; capture actual enqueue/send result and log a correlation id.
- Avoid exposing SMTP usernames/passwords/API keys in wp-admin HTML, frontend JS, logs, repo or screenshots.
- Material mail changes are tested in staging with a capture/test recipient before production.

## Shopify mail
- Shopify-owned transactional notifications remain platform-native unless a custom app/backend use case requires another channel.
- Do not hack storefront Liquid to send server-side mail.
- For custom app/B2B/designer workflows, mail sending belongs in the app/backend/service layer with its own queue/transport/QA.
- Notification-template edits preserve Shopify variables/localization and are preview/tested before live use.

## Template engineering
An email template is a production artifact, not a web page pasted into a body.
- Maintain editable template source separately from generated HTML.
- Render HTML and a meaningful plain-text alternative.
- Use absolute URLs for external assets/links.
- Keep critical content understandable when images are blocked.
- Use semantic hierarchy, readable typography, alt text and sufficient contrast.
- CTA destination and tracking parameters must resolve to the intended environment/domain.
- Personalization data is escaped for its output context and missing optional fields have safe fallbacks.
- Exact brand assets come from the approved brand source of truth.
- Avoid complex web-only CSS/JS assumptions that email clients do not support.

Use React Email when the project already benefits from React/TypeScript component templates; use MJML when a provider-neutral markup/compiler is a better fit. Do not introduce either merely for novelty.

## Email design QA
For important customer-facing templates verify:
- source/template build succeeds
- HTML and plain text render
- subject/preheader/from/reply-to are correct
- mobile and desktop layout
- dark/light behavior where relevant
- Gmail/Outlook/Apple Mail class compatibility appropriate to risk
- image blocking fallback
- links and image URLs
- unsubscribe/preferences links for marketing
- locale/content variables
- long names/long URLs/missing optional data
- accessibility/readability
- no staging/local URLs
- no secrets/debug output

Mailpit-class tools may provide HTML compatibility, link checks, screenshots, API assertions and SMTP chaos/error simulation in local/test environments.

## Local/staging safety
- Development and automated tests must not send to production customer lists.
- Route non-production application mail into Mailpit/test inboxes or an explicit provider sandbox/test mode when possible.
- Maintain an allowlist for any staging relay that can reach external recipients.
- Seed/test addresses are clearly distinguishable from real contacts.
- CI may assert that a given event produced exactly one expected captured message with expected recipient/subject/template markers.

## Form/lead mail reliability
For contact, proposal, B2B or lead forms:
`validate → anti-abuse/rate limit → persist/correlate lead → enqueue mail → provider result/event → user-safe confirmation`.

Do not make email delivery the only copy of a lead. Persist important lead data before/alongside notification so a temporary mail-provider outage does not lose the enquiry.

## Webhook/event handling
- Verify provider webhook signatures/authenticity using the provider's current official method.
- Treat webhook payloads as untrusted input.
- Deduplicate events.
- Store provider/message/event IDs needed for reconciliation.
- Make handlers idempotent and fast; queue expensive follow-up work.
- Handle delivery, bounce, complaint, unsubscribe/suppression and provider-specific failure states when relevant.

## Privacy and security
- Email bodies and recipient addresses are sensitive data.
- Do not log credentials or full message content by default.
- Minimize recipient/content retention in traces and analytics.
- Redact secrets/tokens/provider auth headers.
- Attachments require type/size/source validation; avoid sending arbitrary server paths or untrusted executable content.
- User-supplied headers/from/reply-to fields are constrained to prevent injection/spoofing.

## Observability
For material application mail retain enough metadata to answer:
- which event triggered the message?
- which template/version/locale rendered?
- which provider/message id was used?
- queued/sent/delivered/bounced/complained/suppressed state?
- retry count and last failure category?
- which user/task/order/lead correlation id applies?

Do not equate provider "accepted" with inbox delivery.

## Mail-server/self-hosting gate
Postal/Stalwart/mailcow/docker-mailserver-class infrastructure requires an explicit architecture decision covering:
- domain/IP reputation and warm-up
- DNS/SPF/DKIM/DMARC/PTR/MTA-STS/TLS where applicable
- outbound queue/retry/throttling
- bounce/complaint/abuse handling
- spam filtering and inbound security if receiving mail
- backups, upgrades, monitoring, certificates and incident response
- blocklist/reputation monitoring
- licensing/commercial requirements

If those responsibilities are not justified, use a managed delivery provider.

## Completion gate
A mail change may be `VERIFIED` only when risk-relevant checks pass:
- correct event and recipient
- no duplicate send
- template render + text alternative
- staging/capture test
- provider/transport auth works
- failure/retry behavior tested or inspected
- links/from/reply-to/brand/locale correct
- no secrets/PII leakage
- deliverability/domain configuration checked when changed
- bounce/unsubscribe/suppression path checked when relevant
- production smoke uses a safe test recipient or provider-approved test mechanism
- rollback/config recovery is known for material changes
