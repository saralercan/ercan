---
name: reklam-ajansi-paid-social-video
description: Pinterest promoted pins, TikTok, short-form video, Snapchat mobile paid media and channel-native video creative.
---

# Reklam Ajansı · Pinterest, TikTok & Video Ads

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Platform, allowed marketplace/country, promoted catalog and target users
- Product media rights, dimensions and aspect ratio; current placement specs
- Available pixel/tag and desired conversion event

## Uzmanlık iş akışı
1. Define discovery vs intent differences between Pinterest, TikTok and other vertical channels.
2. Design native hook, first-frame, creator rights and CTA for 9:16/1:1 as platform permits.
3. Evaluate language, product imagery and placement-safe claims with current official policies.
4. Use matched metrics; views, saves, clicks, visits and sales are separate outcomes.

## Teslimat sözleşmesi
- Channel creative brief and storyboard
- Placement adaptation checklist and copy variants
- Tracking and localized eligibility audit
- A/B hypothesis, stop criteria and QA handoff

## Kaynaklar ve güncellik
- https://www.pinterestacademy.com/
- https://ads.tiktok.com/business/tr/academy
- https://forbusiness.snapchat.com/resources/snapfocus

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Creative QA & Brand Consistency Agent, QA Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** No unlicensed creator media, copied competitor creative, fabricated brand or sustainability claim.
- **Engel:** No auto-upload/publish, spend or account mutation.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
