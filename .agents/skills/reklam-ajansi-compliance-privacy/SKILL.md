---
name: reklam-ajansi-compliance-privacy
description: Advertising claims, Google/Meta platform policies, EU GDPR, Turkish KVKK, consent and cross-border advertising restrictions.
---

# Reklam Ajansı · Ads Compliance, Consent & Privacy

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Target country, product vertical, proposed actual copy/targeting and data flows
- Platform policy effective date and documented consent mechanism
- Whether request concerns protected/sensitive claims or regulated products

## Uzmanlık iş akışı
1. Review claims for factual evidence, misleading discounts and prohibited sensitive-targeting assumptions.
2. Audit consent, data minimization, country-specific disclosure and lawful collection for tags and audience exports.
3. Separate a legal interpretation from platform rule and technical implementation; escalate if material ambiguity.
4. Record policy links, market, date and severity; require an external independent final reviewer.

## Teslimat sözleşmesi
- Risk register with exact claim/flow and evidence
- Compliant alternative wording or blocked condition
- Consent and safe tracking checklist
- Escalation to Human Approval and independent security/compliance reviewer

## Kaynaklar ve güncellik
- https://developers.google.com/tag-platform/security/concepts/consent-mode
- https://iabeurope.eu/data-protection-modules/
- https://www.facebookblueprint.com/

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Security & License Agent, QA Agent, Human Approval Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** Do not send customer PII to generative prompts or source/eval logs.
- **Engel:** Do not interpret consent mode as a blanket legal basis; never self-certify compliance.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
