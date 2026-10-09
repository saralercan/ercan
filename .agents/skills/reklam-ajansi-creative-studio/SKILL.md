---
name: reklam-ajansi-creative-studio
description: Original advertisement copy, visual briefs, offer messaging, product image accuracy, typography and A/B creative testing.
---

# Reklam Ajansı · Campaign Creative Studio

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Approved brand identity and actual product features, photos, prices and availability
- Target platform, target audience, language/country and landing page
- Legal rights to user media; requested size, format and output medium

## Uzmanlık iş akışı
1. Form three genuinely different creative angles without inventing price, stock, promotion or product properties.
2. Preserve real photos and brand standards; create native language copy and platform-specific layouts.
3. Use truthful hooks, hierarchy, CTA, proof and landing continuity; make hypotheses testable.
4. Send visuals/copy to an independent reviewer; user approval and account permissions are separate from creative QA.

## Teslimat sözleşmesi
- Three differentiated creative directions with target KPI hypothesis
- Channel-specific copy and visual/storyboard briefs
- A/B matrix with controlled variable and objective
- Independent QA handoff and production-ready draft, not publication

## Kaynaklar ve güncellik
- https://www.facebookblueprint.com/
- https://www.pinterestacademy.com/
- https://ads.tiktok.com/business/tr/academy

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Creative QA & Brand Consistency Agent, QA Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** Do not impersonate brand endorsements or manufacture reviews.
- **Engel:** Do not automatically publish or claim generated image is real product photography.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
