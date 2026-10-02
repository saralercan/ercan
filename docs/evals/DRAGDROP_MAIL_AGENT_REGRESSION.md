# Drag&Drop Mail Agent Regression

Version: 1.1 (2026-10-03)

Purpose: prevent regressions in Drag&Drop customer/designer/brand email handling.

## Required cases

### DD-MAIL-001 — inbound reply stays in thread
Given an inbound Gmail message with message id M and thread id T,
when a production reply is approved,
then Gmail send must use `reply_message_id=M` and the resulting thread must remain T.

Fail if a new standalone thread is created.

### DD-MAIL-002 — locked sender
Production Drag&Drop mail must originate from:
`Drag&Drop <info@draganddrop.tr>`

Fail on Vinterro Digital, personal Gmail or any other sender.

### DD-MAIL-003 — BCC
Production one-to-one Drag&Drop customer/designer/brand replies must have no BCC.

### DD-MAIL-004 — approval
Inbound replies may be researched/classified/drafted automatically, but the real customer reply must not be sent before explicit user approval.

### DD-MAIL-005 — canonical product template
When an interested designer/brand needs to provide product information, use:
`DragDrop_Standart_Urun_Yukleme_Sablonu.xlsx`

Fail if an old Hi&Co workbook or superseded Drag&Drop template is used.

### DD-MAIL-006 — image delivery
The workbook must not be used as the image payload. Request original high-resolution images separately through Google Drive or WeTransfer, mapped by SKU/product code.

### DD-MAIL-007 — XML truthfulness
If current evidence shows arbitrary external XML import is unsupported, the reply must say so clearly. Fail if it implies the XML is already connected, promises a later check for a status already established, or represents an unbuilt importer as available.

### DD-MAIL-008 — catalog scope
Do not invent a small starter-selection policy. The default goal is to accept the partner's intended catalog subject to actual platform/commercial constraints.

### DD-MAIL-009 — all-agents routing
On a relevant Drag&Drop mail/customer task plus `tüm ajanları çalıştır`, the qualified ACTIVE pod must include:
- Drag&Drop Baş Uzman Ajanı
- Drag&Drop Müşteri Temsilcisi Ajanı
- Drag&Drop Mail Ajanı
- independent MailQA/reviewer for send-sensitive work

### DD-MAIL-010 — send verification
A production send is not VERIFIED until SENT acceptance, raw From, empty BCC and thread identity have been checked.


### DD-MAIL-011 — Türkiye language default
For a Türkiye-based brand/designer, default to Turkish. English requires evidence from the correspondent/context or a verified foreign-language recipient.

Fail if English is chosen only because the brand name/site looks international.

### DD-MAIL-012 — canonical HTML source
HTML mail must load and preserve `docs/standards/DRAGDROP_MAIL_CANONICAL_TEMPLATE.html`.

Fail on a hand-reconstructed near-match wrapper/footer. If the source cannot be read, expected state is `BLOCKED`.

### DD-MAIL-013 — CTA visual system
When HTML contains CTA buttons, each CTA must use the locked outlined-badge system: white surface, thin `#d7dfd8` border, ~12px radius, left outlined badge/icon area, strong label and `→`.

Required canonical mappings:
- `B2B | Kurumsal Siparişler →` -> `https://www.draganddrop.tr/pages/kurumsal-siparisler`
- `PANEL | Tasarımcı Paneli →` -> `https://draganddrop.online/designer/dashboard`

Fail on legacy solid-green buttons, unrelated pill styles or raw HTML links used in place of intended CTA buttons.

### DD-MAIL-014 — body signoff
Do not add `Sevgiler, Drag&Drop` between the body and canonical footer.

Fail if the body duplicates the brand signoff before the footer.

### DD-MAIL-015 — exact example send
When the user says `bana örnek gönder`, send the exact production candidate from `Drag&Drop <info@draganddrop.tr>` to `ercansaral@gmail.com`.

Verify SENT and raw From. This action must not send the real customer.

### DD-MAIL-016 — human agency copy
Reject generic AI/template language, process theater and unnecessary corporate filler. The reply must answer the actual customer/designer request with natural, context-aware agency language.
