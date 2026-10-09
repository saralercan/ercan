---
name: reklam-ajansi-analytics-attribution
description: GA4, Google Ads conversion, Meta Pixel/CAPI, Shopify Purchase, event deduplication, attribution and geo incrementality.
---

# Reklam Ajansı · Measurement, Pixel, ROAS & Incrementality

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Original sales/order source, event configuration and attribution settings
- Date/timezone, currency and aggregation grain; consent status
- Account-authorized read-only logs or explicitly state unavailable

## Uzmanlık iş akışı
1. Map end-to-end: product page -> add to cart -> checkout -> Purchase -> analytics and ads conversions.
2. Deduplicate client and server events, check identical currency, order id, value and consent rules.
3. Reconcile actual ecommerce revenue with platform-attributed conversions without summing attributions.
4. Treat lift/iROAS as causal questions requiring holdout, randomized geo or validated quasi-experiment; check power.

## Teslimat sözleşmesi
- Measurement map and evidence-matrix with true/false/unknown per diagnostic
- Event QA and attribution discrepancy table
- Incrementality feasibility assessment; forecast uncertainties
- Independent reviewer proof requirements

## Kaynaklar ve güncellik
- https://developers.google.com/tag-platform/security/concepts/consent-mode
- https://research.google/pubs/measuring-ad-effectiveness-using-geo-experiments/
- https://github.com/google/meridian
- https://github.com/facebookincubator/GeoLift

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Analytics & Attribution Agent, QA Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** 0 purchases does not automatically mean broken tracking.
- **Engel:** No fake Purchase events to production, no exposing customer PII, no causal claim solely from ROAS.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
