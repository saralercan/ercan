---
name: reklam-ajansi-meta-ads
description: Facebook and Instagram ad planning, Ads Manager review, Pixel/Conversions API, lead/sales campaigns and experiment setup.
---

# Reklam Ajansı · Meta Ads & Pixel/CAPI

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Connected business/account, ad account identifier and authorized objective
- Campaign/ad set and creative states from actual Meta account if available
- Pixel/CAPI event ids, event time, attribution window, consent posture

## Uzmanlık iş akışı
1. Draft objective, conversion location, placements, audiences and campaign/ad-set segmentation without unsupported optimization claims.
2. Audit Pixel, server events and event_id dedupe; compare Shopify orders and Ads Manager attributed purchases.
3. Define a hypothesis and measurable test with control where possible; distinguish attributed ROAS from incremental ROAS.
4. Separate daily aggregate budget from each ad set, and calculate totals before proposing; never assume CAPI solves attribution.

## Teslimat sözleşmesi
- Draft campaign/ad set structure and allocation
- Pixel/CAPI Purchase verification checklist with tested versus unknown flags
- Creative/placement requirements and consent risk
- Experiment plan and independent reviewer handoff

## Kaynaklar ve güncellik
- https://www.facebookblueprint.com/
- https://github.com/facebook/facebook-python-business-sdk
- https://agencies.facebookblueprint.com/student/path/211547-meta-pixel-conversions-api-course

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Analytics & Attribution Agent, Marketing compliance via Reklam Ajansı compliance skill, QA Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** No draft is proof of actual Meta account change or real Pixel test.
- **Engel:** No publishing, campaign enable/pause, budget, targeting or audience uploads without scoped approval.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
