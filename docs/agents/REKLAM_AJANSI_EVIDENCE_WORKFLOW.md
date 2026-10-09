# Reklam Ajansı — Kanıtlı İş Akışı / Alt Skill Orkestrasyonu

**Durum:** Planlama altyapısı etkin, gerçek çalışan ajan kanıtı **yok**. Tek kanonik ajanın adı **Reklam Ajansı** (UUID `b2acac02-29d7-418c-9f04-24552e947776`). Dokuz alt skill yetenek alanlarıdır; yeni kullanıcı hesabı, bağımsız ajan veya ilave ücretli worker oluşturmaz.

## Görev hattı

```text
Kullanıcı isteği
   |
   v
1. Intake: amaç, marka, ülke, para birimi, yetki, kaynak mevcudiyeti
   |
   v
2. Birincil skill + en çok 2 destek skill (görev yönlendiricisi)
   |     \       /
   |     kanıtlı araştırma (ancak gerçek worker bağlanınca)
   v
3. Evidence Synthesis: tek birleşik karar/çalışma raporu
   |
   v
4. Independent QA: başka reviewer; henüz PASS değil
   |
   +-- İstenen bir gerçek hesap/para/veri işlemi var mı?
         | evet -> 5. Human Approval / veri erişimi / platform release gate
         | hayır -> Salt-okunur teslimat planı
```

**Not:** Bu akışın ilk aşaması henüz bir `PLAN` oluşturur; herhangi bir reklam API isteği, Google/Meta hesabına erişim, müşteri verisi aktarımı, model çalıştırma, QA PASS, onay veya harcama değildir.

## Kullanım

```bash
# Yalnızca yerel JSON plan çıktısı oluşturur
python3 scripts/plan_reklam_ajansi_workflow.py "Meta Ads Pixel Purchase ve CAPI ölçümünü kontrol et"

# Salt-okunur salt-uzmanlık seçimi
python3 scripts/route_reklam_ajansi_subskills.py "Japonya Shopee reklam uygunluğu ve feed analizi"
```

Çıktıda `stages[]`, `depends_on[]`, `selected_skill_ids[]`, `deferred_skill_ids[]`, `scope_split_recommended`, `gates`, `sensitive_customer_data_requested` ve `human_approval_required` yer alır.

### Örnekler

| Kullanıcı isteği | Gereken kanallar | Bağımsız inceleme |
|---|---|---|
| Meta Pixel Purchase tutarlılığı | Meta Ads + Analitik & Atıf | Analytics & Attribution Agent / QA Agent |
| Google Search reklam taslağı | Google Ads; veri gerekirse Analitik | QA Agent |
| Pinterest video kampanya kreatifi | Ücretli Sosyal Video + Kreatif Stüdyo | Creative QA & Brand Consistency Agent |
| Dünya pazarında katalog reklamları | Küresel Araştırma + Pazaryeri Reklamları | Research Agent + Local SEO & Merchant Agent |
| Bütçe ve dönüşüm iyileştirme | Büyüme & Bütçe + Analitik | Finance Expert Agent / QA Agent |
| KVKK izni veya müşteri kitlesi yükleme | Uyumluluk & Gizlilik | Security & License Agent ve Human Approval Agent |

## Kanıt ve dosya formatı

Her alt skill çıktısı tamamlandığını iddia etmeden önce `source_url`, `source_checked_at`, `account_evidence_origin`, `factual_observations`, `assumptions`, `uncertainties`, `material_policy_risks`, `deliverable_files` ve gerçek yürütücü varsa `provider_receipt` belirtmelidir. Bunlar çalışma standartlarıdır, örnek veya hayalî değerlerle doldurulmamalıdır.

Birleştirme aşamasında:

1. Çelişen sayılar ve farklı platform attribution pencereleri gizlenmez.
2. `Shopify satışları`, `platforma atfedilen ROAS` ve `nedensel ek satış` ayrıdır.
3. En fazla üç alt skill doğrudan planda seçilir. Daha fazla eşleşen uzmanlık `deferred_skill_ids[]` içinde görünür; otomatik olarak tamamlandı sayılmaz. Gerekirse görev iki ayrı plana ayrılır.
4. Bağımsız reviewer, oluşturan ana ajan değildir. Görüş ayrılığı Arbiter’a çıkar.
5. Kullanıcı onayı teknik erişimi, yasal dayanağı veya bütçe sınırını tek başına doğrulamaz.

## Canlı yayın sınırı

- **Reklam yayımlama/durdurma/aktifleştirme, teklif/bütçe değiştirme, müşterinin kişisel verilerini yükleme, ödeme/faturalandırma değiştirme:** her zaman ayrı açık onay, doğru hesabın erişim izni ve canlı release gate.
- `first_touch_email_gate=BLOCKED` değişmez.
- Ajan yürütücüsü henüz aktif olmadığından `provider_receipt_verified=false` ve `independent_qa_done=false` kalır. Bunlar gerçek çalışma yapılmadan değiştirilemez.
- CI yazılım testinin geçmesi, canlı reklam kampanyasının çalıştığını veya çalışan AI modelinin sınavı geçtiğini **kanıtlamaz**.

## Teknik izler

- Kanonik yönlendirici: `docs/agents/REKLAM_AJANSI_SUBSKILL_ROUTER.json`
- Risk/kanıt akışı: `scripts/plan_reklam_ajansi_workflow.py`
- 9 SKILL.md: `.agents/skills/reklam-ajansi-*/SKILL.md`
- Ürün standardı: `docs/agents/REKLAM_AJANSI.md`
- Regression: `tests/test_reklam_ajansi_evidence_workflow.py`
