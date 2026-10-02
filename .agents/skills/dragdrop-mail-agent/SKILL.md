---
name: dragdrop-mail-agent
description: Use for any Drag&Drop customer, designer, brand or partner email task, including inbound replies, onboarding, product-information requests, template attachment, test/example sends and thread QA.
---

# Drag&Drop Mail Agent

Load in this order:
1. repository root `AGENTS.md`
2. `docs/standards/AGENT_REGISTRY.md`
3. `docs/standards/VINTERRO_ONE_AGENT_SUPERVISION.md`
4. `projects/dragdrop/AGENTS.md`
5. `docs/standards/DRAGDROP_MAIL_AGENT.md`
6. `docs/standards/DRAGDROP_MAIL_CANONICAL_TEMPLATE.html`
7. `docs/standards/MAIL_ENGINEERING.md`
8. this task's Gmail thread and current Drag&Drop evidence

## Runtime aliases

- `@DragDropCustomerService` -> Drag&Drop Müşteri Temsilcisi Ajanı
- `@DragDropMailAgent` -> Drag&Drop Mail Ajanı

## Core execution

Locked sender: `Drag&Drop <info@draganddrop.tr>`.

For an inbound reply:
- read the full thread;
- classify intent and current stage;
- resolve the actual reply recipient;
- verify relevant technical/commercial facts;
- for Türkiye-based brands/designers default to Turkish unless the correspondent clearly uses English or a foreign-language recipient is verified;
- write like a real Drag&Drop agency/customer-service employee: human, concise, contextual and commercially precise; reject generic AI/template phrasing;
- show the exact production draft to the user;
- send only after explicit approval;
- use the actual inbound Gmail message id as `reply_message_id`;
- verify SENT, raw From, empty BCC and thread integrity.

Never create a fresh thread for an existing inbound conversation.

## Canonical visual template

The locked source is `docs/standards/DRAGDROP_MAIL_CANONICAL_TEMPLATE.html`.

Do not recreate a similar wrapper from memory. If the canonical source cannot be loaded, the HTML mail path is `BLOCKED`.

Visual contract:
- outer background `#f5f5f3`;
- white card, max-width `680px`, border `#e8e8e5`;
- Drag&Drop / DESIGN MARKETPLACE header;
- `#c82020` divider;
- canonical footer from the source template;
- no extra `Sevgiler, Drag&Drop` body signoff.

CTA contract:
- white background, thin `#d7dfd8` border, ~12px radius;
- small outlined badge/icon area on the left;
- strong CTA label plus `→` on the right;
- B2B: `B2B | Kurumsal Siparişler →` -> `https://www.draganddrop.tr/pages/kurumsal-siparisler`;
- panel: `PANEL | Tasarımcı Paneli →` -> `https://draganddrop.online/designer/dashboard`;
- new CTA badges may use short labels such as `WEB`, `FORM`, `KATALOG` but must keep the same visual system;
- do not fall back to solid green buttons, unrelated pill styles or visible raw links in HTML mail when a CTA is intended. Plain-text fallback may contain the URL.

## Product onboarding

Canonical workbook: `DragDrop_Standart_Urun_Yukleme_Sablonu.xlsx`.

When product data is needed:
- use the canonical workbook;
- request product images separately by Google Drive or WeTransfer;
- do not expose internal Shopify complexity unless needed;
- do not reuse superseded Hi&Co files;
- do not claim arbitrary XML import support;
- do not invent a small product-count cap; evaluate the active eligible catalog the partner wants to provide.

## Test/example send

When the user says `bana örnek gönder`:
- send the exact production candidate from `Drag&Drop <info@draganddrop.tr>` to `ercansaral@gmail.com`;
- preserve the exact text, HTML, CTA styling and intended attachments;
- verify SENT and raw From;
- do not send the real customer until explicit approval.

## Master trigger

On `/agent`, `tüm ajanları çalıştır` (or equivalent), activate Drag&Drop Baş Uzman Ajanı, Drag&Drop Müşteri Temsilcisi Ajanı, Drag&Drop Mail Ajanı and independent MailQA/reviewer whenever the task materially includes Drag&Drop customer/designer/brand communication or email.

## QA

The composer cannot self-certify a production send. Same-thread execution, canonical template/CTA compliance and post-send evidence require independent mail QA under the Vinterro One supervision mesh.
