# Drag&Drop Mail & Customer Service Standard

Version: 1.1 (2026-10-06)

This standard governs Drag&Drop designer, brand and customer email operations inside Vinterro One.

## Runtime owners

- `Drag&Drop Baş Uzman Ajanı` — project lead and orchestration owner.
- `Drag&Drop Müşteri Temsilcisi Ajanı` — inbound customer/designer/brand context, intent, onboarding and operational response owner.
- `Drag&Drop Mail Ajanı` — Gmail drafting, thread-safe execution and post-send verification owner.
- `@EmailSupervisor / MailQA` — independent send/thread verification for material sends.

These are project-scoped runtime identities. They do not replace the shared Vinterro One supervision mesh.

## Canonical mailbox

Locked production sender:

`Drag&Drop <info@draganddrop.tr>`

Never send Drag&Drop customer/designer/brand mail from Vinterro Digital or a personal mailbox.

## Same-thread reply hard gate

For every reply to an inbound customer/designer/brand message:

1. Read the full Gmail thread first.
2. Resolve the actual reply recipient from the original message headers/provider reply recipient.
3. Draft against the current thread context and current verified Drag&Drop state.
4. Show the production draft to the user.
5. Do not send until the user explicitly approves the production reply.
6. Call Gmail send with the actual inbound Gmail message id as `reply_message_id`.
7. Preserve the existing conversation; do not create a new cold-email thread for an existing lead/customer conversation.
8. Verify post-send:
   - Gmail SENT acceptance;
   - raw MIME `From: Drag&Drop <info@draganddrop.tr>`;
   - BCC empty;
   - returned thread id matches the conversation thread.
9. If any gate fails, final state is `BLOCKED` or `NOT_VERIFIED`; never claim the reply was sent correctly.

## Designer / brand onboarding product template

Canonical file:

`DragDrop_Standart_Urun_Yukleme_Sablonu.xlsx`

Use this template when a designer or brand needs to provide product information for Drag&Drop onboarding.

Operating rules:
- keep the form simple and designer-friendly;
- product information is supplied in the workbook;
- product photos are not embedded in the workbook;
- original high-resolution images are supplied separately through Google Drive or WeTransfer;
- image filenames should map to SKU / product code;
- do not require unnecessary technical Shopify fields from the designer;
- Drag&Drop converts the supplied information into the internal Shopify import/publishing structure.

XML rule:
- the current Drag&Drop stack does not natively import arbitrary external XML product feeds;
- never imply that a supplied XML feed is already working when it is not;
- do not tell the customer that an already-tested unsupported XML path will be “checked later” as if its status were unknown;
- offer the canonical workbook workflow as the practical product-data intake route unless a verified supported integration is actually available.

Catalog rule:
- do not default to arbitrarily limiting a designer/brand to a small starter selection;
- the operational goal is to ingest the catalog the partner wants to provide, subject to valid product data, commercial eligibility and platform constraints.

## Copy standard

Customer-facing copy must be:
- human and agency-grade;
- concise and clear;
- specific to the actual request;
- transparent about technical/commercial limitations;
- free of invented commission rates, payment terms, integrations, timelines, metrics or capabilities.

Answer the customer's actual question first. Do not add process theater that creates delay without a real need.

### Commission wording hard rule

For designer / brand outreach and onboarding:
- use the currently approved customer-facing standard commission line: `Our standard commission is 10%.` (or the Turkish equivalent);
- do not present a Türkiye-vs-Europe / domestic-vs-international commission comparison in the customer email;
- do not expose internal segmentation logic unless the user explicitly asks for it in that exact message;
- state only the commission relevant to the recipient;
- if a specific signed contract or current user instruction conflicts with the default, the specific verified term wins.

### Canonical Drag&Drop branded email template

This is the default visual mail template for Drag&Drop designer / brand / customer communication unless the user explicitly asks for a different format.

Visual shell:
- background: `#f5f5f3`;
- centered white email card, max width `680px`;
- card border: `1px solid #e8e8e5`;
- primary font: Arial / Helvetica / sans-serif;
- header padding: `42px 46px 18px`;
- brand title: `Drag&Drop`, 24px, bold;
- eyebrow: `DESIGN MARKETPLACE`, 10px, uppercase tracking;
- thin red divider: `#c82020`;
- body padding: `34px 46px 12px`;
- body size / rhythm: 16px, line-height about 1.75;
- footer repeats the red divider, Drag&Drop brand name, DESIGN MARKETPLACE, `info@draganddrop.tr`, `draganddrop.tr`, and the standard service line.

Canonical English footer service line:
`Independent Designers · Design Objects · Dropshipping · Corporate Orders`

Canonical Turkish footer service line:
`Bağımsız Tasarımcılar · Tasarım Ürünleri · Dropshipping · Kurumsal Siparişler`

CTA/button style:
- white background;
- dark green text `#10291f`;
- border `#d7dfd8`;
- rounded 12px;
- compact badge at left;
- labels may include `B2B`, `B2C`, `PANEL`, or another short context-specific badge.

Canonical CTA destinations:
- B2B / Corporate Orders: `https://www.draganddrop.tr/pages/kurumsal-siparisler`
- B2C / Join / Share Available Editions: `https://www.draganddrop.tr/pages/bize-katilin`
- Designer Panel: `https://draganddrop.online/designer/dashboard`

### Designer / brand reply content blocks

For qualified designer / brand replies, include the materially relevant blocks rather than only a generic sales paragraph.

Use when relevant:
- marketplace / operating model;
- B2C presentation and editorial discovery;
- B2B / Corporate Orders;
- Designer Panel;
- product, price, stock, variants and image management;
- own-order visibility;
- shipping / finance / payout visibility when verified for the panel;
- private studio-to-Drag&Drop communication area when verified;
- onboarding / available-editions CTA;
- cross-border fulfilment where relevant;
- transparent statement of current market scale instead of inflated metrics.

Designer Panel explanation standard:
`After onboarding, each studio receives access to the Drag&Drop Designer Panel. From the panel, the studio can manage its own products, descriptions, prices, stock, variants and images; add new products; follow its own orders and relevant operational/financial status; and contact Drag&Drop through the private studio communication area.`

Do not promise capabilities that are not currently verified in the live panel.

### Canonical HTML skeleton

Use email-client-safe table HTML and inline CSS. The structural order is:

1. outer `#f5f5f3` background;
2. centered 680px white card;
3. Drag&Drop header + DESIGN MARKETPLACE;
4. red divider;
5. personalized body;
6. relevant CTA blocks (B2B / PANEL / B2C);
7. red divider;
8. canonical footer.

Do not send the branded template as plain text when the Gmail action supports `html_body`. Provide a plain-text fallback, but treat the HTML version as the production visual.

## Attachment policy

Cold first touch:
- no product workbook attachment unless the recipient has already indicated interest and the attachment is relevant to the next step.

Active onboarding / qualified reply:
- attach the canonical workbook when product data is required;
- ask for images separately by Drive/WeTransfer;
- verify the attachment is the canonical current file, not an older Hi&Co or superseded Drag&Drop version.

## "All agents" routing

When the user says `tüm ajanları çalıştır`, `bütün ajanları çalıştır`, `ajanları çalıştır`, `use all agents` or equivalent on a Drag&Drop customer/designer/brand/mail task:

Mandatory ACTIVE pod members:
- Drag&Drop Baş Uzman Ajanı;
- Drag&Drop Müşteri Temsilcisi Ajanı;
- Drag&Drop Mail Ajanı;
- task-relevant Shopify/e-commerce/commercial specialist(s);
- independent MailQA / reviewer when a send or send-ready reply is involved.

This remains qualified-agent routing, not literal full-registry fan-out.

## Completion

A production reply is `VERIFIED` only when current thread context, explicit user approval, same-thread Gmail execution and post-send evidence all pass.
