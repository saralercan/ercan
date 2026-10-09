---
name: reklam-ajansi-global-market-research
description: Original-language official platform sources and scholarship for Japan, Korea, China, India, LATAM, MENA, EU, Africa and worldwide markets.
---

# Reklam Ajansı · Worldwide Advertising Research & Native Localization

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Exact market, language, currency and shipping/store eligibility
- User purpose: market scan, campaign research, native ad localization or scientific critique
- Date and provenance of first-party documents, articles and repositories

## Uzmanlık iş akışı
1. Use VINTERRO_GLOBAL_PAID_MEDIA_ACADEMY_TR.md and WORLDWIDE_PAID_MEDIA_SOURCES_2026.json as source maps, not automatic qualifications.
2. Compare country platform mechanisms (LINE Yahoo, Naver/Kakao, Yandex, Mercado, Jumia, Shopee) without assuming Google equivalence.
3. Read official material in original language first; distinguish vendor case, reviewed academic paper and preprint.
4. Flag source conflicts (e.g. Jumia stock rule versions), unclear eligibility, unsupported geographies and regional law.

## Teslimat sözleşmesi
- Region-language-platform evidence matrix with direct source links and review date
- Verified market eligibility assumptions and local-language creative outline
- Scientific critique/experiments if relevant
- Explicit unknowns and local legal/translation review handoff

## Kaynaklar ve güncellik
- https://www.lycbiz.com/jp/seminar/ly-ads/
- https://ads.naver.com/help/faq/161
- https://academy.mercadoads.com/student/catalog?locale=pt-BR
- https://github.com/google/meridian

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Multilingual Localization QA Auditor, Research Agent, QA Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** Don't claim exhaustive world coverage or fabricate local ad platform documentation.
- **Engel:** Do not translate local platform policy into general universal law or auto-spend internationally.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
