# Drag&Drop Mail & Customer Service Standard

Version: 1.3 (2026-10-07)

This standard governs Drag&Drop designer, brand and customer email operations inside Vinterro One.

## Runtime owners

- `Drag&Drop Baş Uzman Ajanı` — project lead and orchestration owner.
- `Drag&Drop Outreach Ajanı` — cold first-touch designer/brand outreach, alphabetical campaign selection, Gmail dedupe and tanışma-mail personalization owner.
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

## Cold first-touch / Tanışma Maili hard route

Canonical skill: `.agents/skills/dragdrop-outreach-intro/SKILL.md` (portable plugin equivalent: `dragdrop-outreach-intro`).

For any cold first-touch designer/brand outreach:
- HARD GATE: subject, plain text and rendered HTML must not contain a commission rate/percentage. This includes existing unsent drafts. Do not auto-recontact already SENT recipients to correct prior commission disclosure;
- activate `Drag&Drop Outreach Ajanı` together with `Drag&Drop Mail Ajanı` and independent MailQA;
- inspect real product/collection evidence before writing the personalized opening;
- never imply prior contact/research history without evidence; do not use unsupported `yeniden inceledik`, `uzun süredir takip ediyoruz` or similar phrasing;
- write at experienced human brand-partnerships/designer-relations level, not generic AI copy;
- separate B2C and B2B opportunity blocks;
- state that Drag&Drop is Türkiye-based but sells internationally, explicitly emphasizing active European sales and suitable Europe-internal / Türkiye-Europe / wider international routes;
- NEVER disclose a commission percentage (including Türkiye's 30% or foreign-partner rates) in an unsolicited first-touch/tanışma email, in any locale. Keep verified rates internal; share the correct commercial rate only after the recipient expresses interest or requests the terms. No monthly fixed/listing fee may be mentioned if still accurate, but do not lead with commercial terms;
- explain operational ownership for stock, order forwarding, preparation/packing/shipping, digital storefront, payment flow, sales process and customer communication;
- preserve canonical B2C Bize Katılın + B2B Kurumsal Siparişler CTAs;
- dedupe every candidate against Gmail SENT by brand + exact email + domain, plus bounce/opt-out/relationship suppression;
- when using a source Excel/list alphabetically, skip non-clean rows and continue until the requested number of unique clean recipients is reached.

When the user requests an example, send the first clean real candidate to `ercansaral@gmail.com` from `info@draganddrop.tr` using the exact production candidate and canonical HTML. Production remains blocked until the user approves the batch/send. Once a specific batch is explicitly approved, per-recipient re-approval is not required unless a material exception changes terms, locale, relationship state or risk.

If the recipient replies or an existing active thread is found, cold-outreach ownership ends and the workflow moves to `Drag&Drop Müşteri Temsilcisi Ajanı` + `Drag&Drop Mail Ajanı` in that same Gmail thread.

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

## Canonical email visual template

For cold first-touch outreach, the **only** approved 1:1 shell is `docs/standards/DRAGDROP_OUTREACH_CANONICAL_TEMPLATE.html`. The general mail template below is for non-cold correspondence and must never replace the outreach shell.

Locked source artifact:

`docs/standards/DRAGDROP_MAIL_CANONICAL_TEMPLATE.html`

The HTML wrapper, divider, footer and CTA construction are source artifacts, not approximate prose guidance. Do not recreate a visually similar email from memory. If the canonical template cannot be loaded, HTML mail rendering is `BLOCKED`.

Canonical visual rules:
- outer background: `#f5f5f3`;
- outer padding: `32px 16px`;
- card: white, max-width `680px`, border `1px solid #e8e8e5`;
- header padding: `42px 46px 18px`;
- header brand: `Drag&Drop`, 24px bold;
- descriptor: `DESIGN MARKETPLACE`, 10px, tracked;
- divider: `1px #c82020`;
- body padding: `34px 46px 12px`, 16px, line-height 1.75;
- footer uses the exact source-template structure and wording;
- do not add `Sevgiler, Drag&Drop` between body and footer.

### Locked CTA system

Every HTML link that is intentionally presented as a CTA button uses the same visual language:
- white background;
- `1px solid #d7dfd8` border;
- about `12px` radius;
- left-side small outlined badge/icon area in `#10291f`;
- strong CTA text plus `→`;
- no solid-green legacy button, unrelated pill style or exposed raw URL in HTML when a CTA is intended.

Canonical CTAs:
- Turkish B2B: `B2B | Kurumsal Siparişler →` -> `https://www.draganddrop.tr/pages/kurumsal-siparisler`
- Turkish panel: `PANEL | Tasarımcı Paneli →` -> `https://draganddrop.online/designer/dashboard`

For non-Turkish recipient locales, the badge, destination URL and locked visual shell remain unchanged; the visible CTA label is localized into the verified recipient language. Additional CTA badges may use short context labels such as `WEB`, `FORM` or `KATALOG`, but the same button shell is mandatory.

### Example/test-send behavior

`bana örnek gönder` means:
- send the exact production candidate to `ercansaral@gmail.com`;
- sender remains `Drag&Drop <info@draganddrop.tr>`;
- text, HTML, CTA design and intended attachments must match the production candidate 1:1;
- verify SENT and raw MIME From;
- do not send the real customer until the user separately approves production send.

## Locale routing hard gate

Before drafting any first-touch or reply, resolve `recipient_locale` from current evidence:
1. verified business country;
2. official website/contact-page language;
3. current Gmail thread language, when a conversation already exists.

Cold outreach uses the recipient's verified local business language by default. Country examples include Türkiye→Turkish, Greece→Greek, Bulgaria→Bulgarian, Germany/Austria→German, Italy→Italian, France→French, Spain→Spanish, Romania→Romanian, Georgia→Georgian, Sweden→Swedish, Norway→Norwegian, Denmark→Danish and Finland→Finnish.

For multilingual countries/brands, use the language evidenced by the official site/contact channel or the correspondent. English is not the default foreign-outreach language. It is permitted only when the brand/correspondent clearly uses English, explicitly requests English, or no exact local-language route can be verified. When the user requires local-language outreach and the locale cannot be verified, production send is `BLOCKED` rather than silently falling back to English.

Every non-Türkiye production mail must route through the exact-match locale specialist / `@LocalizationEditor` and an independent same-language copy reviewer before MailQA/release. The canonical HTML wrapper remains unchanged; only body/compliance slots and visible CTA labels are localized.

## Copy standard

Customer-facing copy must be:
- human and agency-grade;
- written like a real Drag&Drop agency/customer-service employee, not an AI template;
- compliant with the Locale routing hard gate above;
- concise and clear;
- specific to the actual request;
- transparent about technical/commercial limitations;
- free of invented commission rates, payment terms, integrations, timelines, metrics or capabilities.

Answer the customer's actual question first. Do not add process theater that creates delay without a real need.

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
- Drag&Drop Outreach Ajanı when cold first-touch/outreach is in scope;
- Drag&Drop Müşteri Temsilcisi Ajanı;
- Drag&Drop Mail Ajanı;
- exact-match locale specialist / `@LocalizationEditor` for every non-Türkiye recipient;
- task-relevant Shopify/e-commerce/commercial specialist(s);
- independent same-language copy reviewer plus MailQA / reviewer when a send or send-ready reply is involved.

This remains qualified-agent routing, not literal full-registry fan-out.

## Completion

A production reply is `VERIFIED` only when current thread context, explicit user approval, same-thread Gmail execution and post-send evidence all pass.
