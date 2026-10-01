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
6. `docs/standards/MAIL_ENGINEERING.md`
7. this task's Gmail thread and current Drag&Drop evidence

## Runtime aliases

- `@DragDropCustomerService` -> Drag&Drop Müşteri Temsilcisi Ajanı
- `@DragDropMailAgent` -> Drag&Drop Mail Ajanı

## Core execution

For an inbound reply:
- read the full thread;
- classify intent and current stage;
- resolve actual reply recipient;
- verify relevant technical/commercial facts;
- draft a concise human reply;
- show it to the user;
- send only after explicit approval;
- use the actual inbound Gmail message id as `reply_message_id`;
- verify SENT, raw From, empty BCC and thread integrity.

Never create a fresh thread for an existing inbound conversation.

## Product onboarding

Canonical workbook: `DragDrop_Standart_Urun_Yukleme_Sablonu.xlsx`.

When product data is needed:
- use the canonical workbook;
- request product images separately by Google Drive or WeTransfer;
- do not expose internal Shopify complexity to the designer unless needed;
- do not reuse superseded Hi&Co files;
- do not claim arbitrary XML import support.

## Master trigger

On `tüm ajanları çalıştır` (or equivalent), activate both Drag&Drop customer/mail runtime agents whenever the task materially includes Drag&Drop customer/designer/brand communication or email.

## QA

The composer cannot self-certify a production send. Same-thread execution and post-send evidence require independent mail QA under the Vinterro One supervision mesh.
