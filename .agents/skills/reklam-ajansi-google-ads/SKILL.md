---
name: reklam-ajansi-google-ads
description: Google Ads Search, Performance Max, Shopping, Merchant Center, keyword planning and platform audit. Triggers: Google Ads, PMax, Shopping, merchant feed, search terms, negative keywords.
---

# Reklam Ajansı · Google Ads & Search/Shopping

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Store/catalog and actual campaign access scope; objective, country, language, currency
- Existing campaign state, budgets, bidding and conversion definitions; identify unknowns
- Merchant products/variant/price/shipping country compatibility where relevant

## Uzmanlık iş akışı
1. Separate Search brand, nonbrand, Shopping and PMax hypotheses; never assume they should all launch.
2. Draft intent clusters, negatives, landing-page mappings, query exclusions and feed QA with source labels.
3. Compare observed conversion events against shop orders; don't diagnose broken purchase tracking from zeros alone.
4. Use official account-level keyword metrics only if actually connected; otherwise leave CPC, volume and forecasts explicitly unknown.

## Teslimat sözleşmesi
- Read-only account readiness checklist
- Campaign/ad-group/keyword proposal with evidence and exclusions
- QA table: conversion, consent, feed, landing page, currency, region
- Potential mutation diff for human approval, never a live change

## Kaynaklar ve güncellik
- https://skillshop.withgoogle.com/googleads/
- https://developers.google.com/google-ads/api/docs/keyword-planning/generate-keyword-ideas
- https://developers.google.com/google-ads/api/samples

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Analytics & Attribution Agent, QA Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** Do not change budgets, activate ads, call recommendation.apply(), create Shopping feeds or campaigns.
- **Engel:** Never invent keyword search volume, CPC, ROAS or Google account diagnostics.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
