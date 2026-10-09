---
name: reklam-ajansi-growth-budget
description: Budget scenario planning, CAC/LTV, Shopify unit economics, media mix, CRO and growth forecasts without unapproved spend.
---

# Reklam Ajansı · Growth, Unit Economics & Budget Scenarios

**Kimlik:** Ana ajan yalnızca `Reklam Ajansı` (`b2acac02-29d7-418c-9f04-24552e947776`). Bu dosya bağımsız çalışan ajan değil, kanıt ve teslimat yükümlülükleri ayrı bir **alt skill**dir.

## Amaç ve aktivasyon
Yalnızca ilgili kullanıcı niyeti ve kaynaklar eşleşince yükle. Çok disiplinli işler için `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json` üzerinden 1 ana + en fazla 2 destek skill seç; bağımsız dış QA gerekiyorsa mevcut QA Agent'i seç. Aynı anda planlama yapmak, birden fazla doğrulanmış model yürütücüsü olduğu anlamına gelmez.

## Gerekli girdiler
- Observed sales, gross margin, taxes, shipping, refunds, service fees and allowable CPA
- Actual current daily/monthly paid budgets; period, geography, currency
- Tracking quality and experimental maturity, not just platform recommendations

## Uzmanlık iş akışı
1. Compute gross contribution and breakeven CPA/ROAS from supplied real unit economics; label assumed numbers.
2. Present conservative/base/aggressive scenarios with sensitivity and stop-loss rules.
3. Consider creative, landing page, logistics and regional split; prioritize experiments over blind scale.
4. Use MMM only when timeseries/geo variation are sufficient and model diagnostics accept; otherwise label infeasible.

## Teslimat sözleşmesi
- Budget scenarios and sensitivity table, without modifying platform
- Funnel/CRO priority matrix tied to accountable KPI
- Guardrail thresholds, assumptions and uncertainty ranges
- Explicit decision memo requiring Human Approval Agent for any spend change

## Kaynaklar ve güncellik
- https://github.com/google/meridian
- https://github.com/facebookexperimental/Robyn
- https://research.google/pubs/robust-causal-inference-for-incremental-return-on-ad-spend-with-randomized-paired-geo-experiments/

Görev tarihinde güncel resmî dokümanı ve platform hesabını yeniden denetle; materyalin varlığı eğitim/sertifika veya gerçek hesap denetimi kanıtı değildir. Eski müfredat: `docs/academy/VINTERRO_PAID_MEDIA_ACADEMY_TR.md`. Dünya atlası: `docs/academy/WORLDWIDE_PAID_MEDIA_SOURCES_2026.json`.

## QA ve yürütme sınırı
İlgili bağımsız inceleyici: Finance Expert Agent, Analytics & Attribution Agent, QA Agent. Skill sahibinin kendi sonucuna PASS vermesi yasaktır. Gerçek ajan değerlendirmesi yalnız kayıtlı yürütücü kanıtı ve bağımsız onay ile mümkündür.

- **Engel:** No total spend increase or automatic campaign launch.
- **Engel:** Never present MMM budget optimizer output as precise with insufficient observations.

**Zorunlu genel kilit:** araştırma/analiz ve onaylı çalışma alanı taslağı dışında live write yok; reklam yayınlama, duraklatma, bütçe, teklif, hedef kitle, faturalandırma veya müşteri verisi değişikliği için ayrıca açık insan onayı, doğrulanmış platform izni ve final release-gate gerekir. Gmail ilk temas durumu `BLOCKED`; skill bu kilidi açamaz.
