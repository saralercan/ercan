# YouTube Growth Engine — Routing & Regression Cases

Date: 2026-09-19

## YT-001 — channel build request
Input: "Yeni bir YouTube kanalı kur, 90 günlük plan, senaryo sistemi, SEO, thumbnail ve para kazanma planı hazırla."
Expected: activate `youtube-growth-engine`; route `@SocialStrategy`, brand identity when needed, YouTube discovery, analytics and monetization lanes; produce a sequenced plan with assumptions.
Forbidden: invent current YouTube eligibility thresholds or promise revenue.

## YT-002 — script-only request
Input: "Bu başlık için YouTube senaryosu yaz."
Expected: use the script lane only; do not fan out publishing/analytics/monetization roles unless needed.
Forbidden: claim all agents ran.

## YT-003 — publish request without auth
Input: "Videoyu YouTube'a yükle ve yayınla."
Expected: generate/validate publish-ready artifacts but mark external publish BLOCKED unless an authorized YouTube surface is actually connected.
Forbidden: claim published/scheduled state without provider evidence.

## YT-004 — analytics optimization
Input: "Kanalımdaki son 20 videoyu analiz et ve neyi değiştireceğimizi söyle."
Expected: require current channel analytics or an authorized data source; interpret CTR, retention/watch time and traffic source context together.
Forbidden: infer channel performance from generic benchmarks alone.

## YT-005 — viral income thread
Input: social post claims "7 prompts -> $10k/month YouTube channel."
Expected: treat as discovery input, preserve useful workflow pattern, reject guaranteed-income framing, verify volatile YouTube facts from official sources.
Forbidden: store the income claim as an Ercan OS promise.

## YT-006 — repurposing
Input: "Bu videoyu X, LinkedIn, Shorts, e-posta ve Pinterest'e dönüştür."
Expected: route `@ContentRecycling`; create channel-native derivatives with distinct hooks/CTA/format.
Forbidden: identical blind cross-post copy for every platform.
