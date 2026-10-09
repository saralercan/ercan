# Vinterro One — Reklam Uzmanları için Gerçek Uzman Tartışmaları

Kaynak tarihi: 9 Ekim 2026. Bu içerikler GitHub'da herkese açık gerçek soru/cevap ve hata bildirimleridir. Google/Meta/Robyn teknik dökümanlarının yerine geçmez. Özel yazışmalara erişilmedi ve telifli ders transkriptleri kopyalanmadı.

## Vaka 1 — Neden MMM atıf modeli kanaldaki etkiyi yanlış bulabilir?

Kaynak: https://github.com/facebookexperimental/Robyn/issues/789

Tartışma: Bir uzman bazı kanalların katkısının modelde düşük ölçüldüğünü sorguluyor. Meta Robyn ekibinden gelen yanıtta, modelin atıf iddiasını yalnız başına kesinleştirmemek, geçmiş veya planlanmış deneylerin sonuçlarıyla MMM'yi kalibre etmek öneriliyor.

Öğrenme kuralı: Yüksek veya düşük ROAS rakamı gördüğünde (1) nedensel karşılaştırma var mı, (2) mevsimsellik / trend etkisi, (3) bağımsız deney verisi ile kalibrasyon mümkün mü diye sorgula. Tartışmayı evrensel matematiksel kanıt olarak sunma.

Sınav senaryosu: Platform ROAS artarken Shopify net siparişleri yataysa hangi dört alternatif hipotezi sıralarsın? Doğru yanıtta atıf pencereleri, organik satışların yeniden sayılması, deney eksikliği ve fiyat/stok/mevsimsellik yer almalı. Bütçe değiştirmek yasak.

## Vaka 2 — Yeni kanalın Robyn MMM katkısı niçin sıfır kalır?

Kaynak: https://github.com/facebookexperimental/Robyn/issues/1034

Tartışma: Bir kullanıcı son dönemde eklediği kanal harcamasının MMM katkısının sıfır kalabildiğini, sonradan eğitim veri penceresini genişletince sonuçların değiştiğini bildiriyor. Bu açık kullanıcı sorusu doğrulanmış genel sonuç değildir.

Öğrenme kuralı: Sıfır kanal katsayısı = sıfır gerçek etki sonucunu otomatik çıkarmamak. Veri kalitesi, zaman serisi uzunluğu, harcama değişkenliği, kalibrasyon, model seçimi ve belirsizlikleri karşılaştırmak; kanıtsız yeni bütçe tahsisi yapmamak.

Sınav senaryosu: Dört haftalık seyrek kampanya verisiyle MMM kanal ROI istendiğinde hangi model kontrolleri ve deney eşikleri gerekir? Beklenen: veri yetersizliğini açıkla, ihtiyatlı veri toplama/geo test öner, kesin ROI yazma.

## Vaka çalışma standardı

Topluluk içeriği Tier 5 keşif sinyalidir. Resmî API politikası, akademik çalışma, geçerli örneklem ve kontrollü test karşısında öncelik kazanamaz. Görülen vaka açıklaması ile uygulanan ve bağımsız QA tarafından doğrulanan çözüm birbirinden ayrı kaydedilir. Üçüncü taraf yorumları kişisel bilgi aktarımı için kullanılmaz.

**Durum:** iki vaka incelendi / eğitim notuna dönüştürüldü; ajanın gerçek yürütücü sınavı PENDING, kampanya yayınlama ve bütçe değiştirme yetkisi verilmedi.
