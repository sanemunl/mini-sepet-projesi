Phase 3:AI Pair Programming Günlüğü
Tarih: 14.05.2026
Süre: 35 Dakika
Katılımcılar: Sanem Zeynep Ünal & Gemini (AI)
1. Tartışma Konusu: İndirim Mantığı ve OCP
Soru: Sepetteki calculate_total metodu içindeki if-else blokları (YILBASI, OGRENCI vb.) her yeni kampanya geldiğinde sınıfın değiştirilmesine neden oluyor. Bunu Open/Closed Prensibi'ne (OCP) uygun hale nasıl getiririz?
AI Önerisi: İndirim mantığını sepetten tamamen soyutlamak için Strategy Pattern kullanılmalı. DiscountStrategy adında bir soyut arayüz oluşturup, her indirim türünü (Yüzde, Sabit Fiyat vb.) ayrı birer sınıf olarak tanımlamalıyız.
Karar: DiscountStrategy arayüzü ve buna bağlı PercentageDiscount, NoDiscount sınıfları uygulandı. Cart.set_discount_strategy() metodu ile çalışma anında indirim türü değiştirilebilir hale getirildi.
2. Tartışma Konusu:Sistem Etkileşimi ve Observer
Soru: Ürün eklendiğinde stok birimi gibi diğer sistemlerin haberdar olması gerekiyor ama bu sistemleri Cart sınıfına sıkı sıkıya bağlamak istemiyorum. Çözüm ne olabilir?
AI Önerisi: Observer Pattern bu durum için en uygunu. Cart sınıfı "Subject" (Gözlenen) olmalı, stok yöneticisi gibi sınıflar ise "Observer" (Gözlemci) olarak bu sepeti dinlemeli.
AI Değerlendirme Raporu
1. AI olmadan bu faz ne kadar sürerdi?
AI desteği olmadan, Strategy ve Observer örüntülerinin birbirini bozmadan aynı sınıfta (Cart) nasıl koordine edileceğini araştırmak ve hatasız kodlamak yaklaşık 2.5 - 3 saat sürerdi. AI ile kavramsal tartışmaları yaparak kodun iskeletini oluşturmak bu süreyi 30-40 dakikaya indirdi.
2. AI beni nerede yanılttı?
AI, ilk başta Observer bildirimlerini add_item metodunun en başında yapmayı önerdi. Ancak ben, ürün listeye eklenmeden bildirim yapılmasının mantıksal hatalara (stoktan düşüp listede gözükmemesi gibi) yol açabileceğini fark ettim. Bildirimlerin ürün başarıyla listeye eklendikten sonra (metodun sonunda) tetiklenmesi gerektiğini belirterek yapıyı güncelledim.