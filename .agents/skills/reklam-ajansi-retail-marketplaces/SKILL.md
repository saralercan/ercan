---
name: reklam-ajansi-retail-marketplaces
description: Merchant Center product feeds, Amazon Sponsored Products, Mercado Ads, Shopee, Flipkart, Jumia and cross-border retail campaign eligibility.
---

# Reklam Ajansı · Retail Media & Marketplace Shopping Ads

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Verified products, price, stock, variants, image rights and shipping destinations
- Marketplace account eligibility, commission and operating country
- Feed/ads identifier, targeting type and expected customer sale economics

## Uzmanlık iş akışı
1. Compare product-feed fields and store truth; distinguish product QA from paid campaign performance.
2. Validate marketplace brand/store whitelist, item stock, eligibility and current official documentation.
3. Check country-specific return, shipping, sales tax and price consistency.
4. Draft campaign taxonomy, product exclusions, optimization hypotheses and approval-only mutation proposal.

## Teslimat sözleşmesi
- Feed/product readiness audit with market flags
- Marketplace advertiser eligibility checklist
- Product group ad proposal and non-spend test plan
- Independent retail/feed QA handoff

## Kaynaklar ve güncellik
- https://advertising.amazon.com/academy
- https://support.google.com/merchants/answer/14264257?hl=en
- https://academy.mercadoads.com/student/catalog?locale=es-419
- https://vendorhub.jumia.com.ng/seller-academy/sponsored-products/

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Local SEO & Merchant Agent, E-commerce Expert Agent, QA Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** Do not treat the public platform's seller ROI claims as merchant-specific business results.
- **Engel:** Jumia source contradictions require current panel check, never blindly choose 2 or 3 unit requirement; no unapproved campaign creation.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
