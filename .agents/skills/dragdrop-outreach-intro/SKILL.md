---
name: dragdrop-outreach-intro
description: Use for Drag&Drop cold first-touch designer/brand outreach, including alphabetical Excel/list campaigns, dedupe-safe recipient selection, personalized introduction copy, example sends and approved batch sends.
---

# Drag&Drop Outreach — Tanışma Maili Standardı

Owner agent: `Drag&Drop Outreach Ajanı`.

This skill owns **cold first-touch / tanışma outreach** only. Once a recipient replies or an existing conversation is found, hand off to `Drag&Drop Müşteri Temsilcisi Ajanı` + `Drag&Drop Mail Ajanı` and preserve the existing Gmail thread.

## Mandatory load order

1. repository root `AGENTS.md`
2. `projects/dragdrop/AGENTS.md`
3. `.agents/skills/dragdrop-mail-agent/SKILL.md`
4. `docs/standards/DRAGDROP_MAIL_AGENT.md`
5. `docs/standards/DRAGDROP_OUTREACH_CANONICAL_TEMPLATE.html`
6. this skill
7. current source list / Excel and Gmail SENT evidence
8. current public product/collection evidence when the source list does not already provide enough verified product detail

## Locked operating rules

1. İlk temas mailinde gerçek ürün/koleksiyon incelenmiş olacak. Geçmiş temas yoksa “yeniden inceledik”, “uzun süredir takip ediyoruz” gibi geçmiş temas ima eden ifadeler kullanılmayacak.
2. Dil, Vinterro Digital’de çalışan deneyimli bir **brand partnerships / designer relations uzmanı** seviyesinde olacak: doğal, profesyonel, kişiselleştirilmiş ve satış odaklı. Generic AI/template phrasing yasaktır.
3. B2C ve B2B fırsatları ayrı ve açık anlatılacak.
4. Drag&Drop’un **Türkiye merkezli olduğu fakat özellikle Avrupa’ya aktif satış yaptığı** açıkça belirtilecek; Avrupa içi, Türkiye–Avrupa ve diğer uluslararası pazarlar kapsanacak.
5. Türkiye merkezli iş birliklerinde **%30 komisyon**, aylık sabit ücret ve listeleme ücreti olmadığı belirtilecek. Türkiye dışı marka/tasarımcılar için güncel doğrulanmış standart oran `DRAGDROP_MAIL_AGENT.md` içindeki kurala göre uygulanır; yanlışlıkla %30 yazılmaz.
6. Stok, sipariş, hazırlama/kargo ve Drag&Drop’un üstlendiği dijital vitrin, ödeme, satış ve müşteri iletişimi görevleri açık olacak.
7. B2C **Bize Katılın** ve B2B **Kurumsal Siparişler** CTA’ları canonical Drag&Drop mail tasarımıyla korunacak.
8. Mailin giriş paragrafı her tasarımcı/markanın **gerçek ürünlerine / koleksiyonuna / malzeme veya tasarım diline** göre özel yazılacak; gövde standardı korunacak.
9. Mükerrer gönderim yapılmayacak; her adres Gmail SENT geçmişine karşı en az **marka + exact email + domain** bazında kontrol edilecek. Bounce suppression, opt-out ve mevcut ilişki kayıtları da kontrol edilir.
10. Bu yapı **Drag&Drop Outreach — Tanışma Maili Standardı** olarak kullanılacak.

## Candidate selection and alphabetical batch rule

When the user says to proceed alphabetically from a designer Excel/list:
- normalize brand/designer names for sorting without changing the displayed brand name;
- preserve alphabetical order;
- for each row, verify a public/business email and minimum product/category context;
- search Gmail SENT by exact email, domain and brand name;
- skip recipients already contacted, bounced/suppressed, opted out, or already in an active relationship unless the user explicitly requests a relationship-aware follow-up;
- continue down the alphabetical list until the requested number of **clean unique recipients** is reached;
- never backfill a skipped row with an unverified email merely to hit a quota.

## Research truthfulness gate

The personalized opening must be grounded in real evidence.

Allowed evidence:
- the user-provided/current Excel or lead registry;
- the brand/designer’s official website or official product/collection page;
- a verified official social/profile source when needed.

Do not invent:
- products, collections, materials, awards, stock, export history, customer segments, retail partners or prior contact;
- phrases such as “yeniden inceledik”, “uzun süredir takip ediyoruz”, “daha önce konuşmuştuk” unless current evidence proves them.

If no reliable product/collection signal can be verified, **skip the candidate or mark it for enrichment** rather than fabricating personalization.

## Canonical first-touch body contract

The opening paragraph is always recipient-specific. The remaining commercial structure is standardized:

- explain why the collection fits Drag&Drop;
- **B2C:** curated marketplace, relevant categories, New Arrivals/editorial discovery where genuinely applicable;
- **International / Europe:** make clear that Drag&Drop is Türkiye-based but not Türkiye-only, with an explicit emphasis on active European sales and suitable Europe-internal / Türkiye-Europe / broader international routes;
- **B2B:** Corporate Orders / project matching, using only project categories that plausibly fit the recipient;
- **Commercial model:** correct commission by verified legal/tax establishment, no monthly fixed fee, no listing fee;
- **Operations:** stock remains with the brand; order is forwarded; product preparation/packing/shipping stay with the brand unless a verified specific arrangement says otherwise; Drag&Drop handles/supports the digital storefront, payment flow, sales process and customer communication;
- **CTA:** B2C Bize Katılın + B2B Kurumsal Siparişler;
- finish with a low-friction request for current catalogue/product list/collection link.

### Canonical Türkiye / Europe positioning

For Türkiye-based first-touch, preserve this meaning naturally:

> Drag&Drop Türkiye merkezli bir tasarım pazaryeri olmakla birlikte satışlarımızı yalnızca Türkiye ile sınırlamıyoruz. Özellikle Avrupa pazarında aktif olarak satış yapıyor; uygun ürünlerde Avrupa içi, Türkiye’den Avrupa’ya, Avrupa’dan Türkiye’ye ve diğer uluslararası pazarlara satış modellerini değerlendiriyoruz.

Do not repeat it mechanically if the surrounding copy can say the same thing more naturally. The facts and scope must remain intact.

## Locale rule

Follow the Drag&Drop Mail Agent locale gate.
- Türkiye recipient -> Turkish.
- Foreign recipient -> verified local business language by default.
- For foreign production mail, exact-match language specialist / LocalizationEditor + independent same-language QA are required.
- English is not a generic fallback when the verified local language is available.

## Visual and CTA rule

Locked sender: `Drag&Drop <info@draganddrop.tr>`.

Use the canonical branded HTML shell from `docs/standards/DRAGDROP_OUTREACH_CANONICAL_TEMPLATE.html`; do not rebuild it from memory.

Required CTAs:
- B2C / Bize Katılın -> `https://www.draganddrop.tr/pages/bize-katilin`
- B2B / Kurumsal Siparişler -> `https://www.draganddrop.tr/pages/kurumsal-siparisler`

For foreign locales, localize visible labels while preserving badge, destination and visual shell.

## Example and approval gate

When the user says `bana örnek gönder`:
- choose the **first clean alphabetic candidate** under the current list rules;
- compose the real production candidate, not a generic placeholder;
- send the exact candidate from `info@draganddrop.tr` to `ercansaral@gmail.com`;
- verify Gmail SENT and raw From;
- do not send it to the real recipient yet.

After the user explicitly approves a named batch (for example “100 maili gönder”), that approval covers that batch under this exact standard. Do not ask for per-recipient approval again unless a material exception changes commercial terms, recipient relationship state, locale, or content risk.

## Production batch execution

For an approved batch:
- send one recipient at a time; no BCC blast;
- dedupe again immediately before send;
- use the canonical HTML and a plain-text fallback;
- preserve alphabetical progression after every skip;
- record/retain enough evidence to identify sent vs skipped recipients;
- post-send verify provider acceptance and sender identity;
- if Gmail or source evidence becomes ambiguous, stop the affected recipient rather than guessing.

## QA / completion

Mandatory reviewer focus:
- personalization is real, not hallucinated;
- no false prior-contact implication;
- B2C/B2B separation;
- Europe/international positioning present;
- correct commission for recipient establishment;
- no monthly/listing fee claim drift;
- operations split accurate;
- CTA URLs/labels correct;
- dedupe evidence present;
- sender is `info@draganddrop.tr`;
- no BCC;
- locale is correct.

Use `VERIFIED` only when the relevant selection, copy, dedupe and send evidence all pass.
