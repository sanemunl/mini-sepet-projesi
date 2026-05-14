# Faz 0: Başlangıç Kodu Analizi
## Tespit Edilen Tasarım Sorunları

1.Açık/Kapalı Prensibi (OCP) İhlali: Yeni bir indirim türü eklemek için `calculate_total` metodunu değiştirmek gerekiyor.
2.Tek Sorumluluk Prensibi (SRP) İhlali: `Cart` sınıfı hem ürün listesini tutuyor hem de indirim hesaplıyor.
3.Esneklik Eksikliği: İndirim kodları kodun içine sabitlenmiş (hard-coded).
4.Kod Tekrarı Potansiyeli: Benzer indirim mantıkları farklı sınıflarda tekrar edebilir.
5.Test Zorluğu: İndirim mantığını sepetten bağımsız test etmek imkansız.

##AI Karşılaştırması (Faz 0)
Ödev gereği, yazdığım başlangıç kodunu yapay zeka (Gemini) ile paylaştım ve sonuçları kendi listemle kıyasladım.  
AI Ne Gördü?
Sıkı Bağlılık (Tight Coupling): Ürünlerin birer sözlük (dict) yapısında tutulmasının veri bütünlüğünü bozabileceğini ve nesne yönelimli programlama (OOP) avantajlarını engellediğini belirtti.
Ölçeklenebilirlik (Scalability): Mevcut if-elif yapısının aynı anda birden fazla indirimi (kompozisyon) yönetemeyeceğini fark etti.
Sihirli Sayılar (Magic Numbers): Kod içerisindeki indirim oranlarının (0.80, 10, 20) isimlendirilmiş sabitler yerine doğrudan yazılmasının bakım zorluğu yaratacağını ekledi.
Aralarındaki Farklar ve Değerlendirme:
AI ile benim listem büyük oranda örtüşüyor (özellikle SOLID prensipleri konusunda). Ancak AI, kodun "temiz kod"standartlarına daha fazla odaklanırken; ben daha çok "mimari esneklik" üzerine yoğunlaştım.