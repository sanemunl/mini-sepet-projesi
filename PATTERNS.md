Faz 1: Creational (Yaratımsal) Örüntüler
1. Factory Method
Nerede Kullanıldı: src/cart.py içerisindeki ProductFactory sınıfı ve Cart.add_item metodu içerisinde kullanıldı.  
Neden Kullanıldı: Faz 0'da sepet sınıfı (Cart), hangi ürünün nasıl yaratılacağını (if-else bloklarıyla) kendisi biliyordu. Bu durum "God Class" sorununa ve esneklik kaybına yol açıyordu. Nesne yaratma sorumluluğunu sepetten ayırmak için bu örüntü seçildi. 
 Ne Kazandım:Loose Coupling (Gevşek Bağlılık): Sepet artık somut ürün sınıflarına (Electronics, Food) doğrudan bağımlı değil.  
  OCP Desteği: Yeni bir ürün kategorisi eklemek için sepetin kodunu değiştirmeye gerek kalmadı; sadece fabrikaya yeni bir seçenek eklemek yeterli.  
  Single Responsibility: Sepet sadece ürünleri listelemeye, fabrika ise sadece ürünleri üretmeye odaklandı.
![Faz 0 UML](docs/diagrams/faz0.drawio.png)
![Faz 1 UML](docs/diagrams/faz1.drawio.png)

Faz 2:
2. Decorator (Faz 2)
Nerede Kullanıldı: GiftWrapDecorator ve WarrantyDecorator sınıflarında.
Neden Kullanıldı: Ürün sınıflarını (Electronics vb.) kalıtımla şişirmek yerine, çalışma anında (runtime) dinamik özellik eklemek için.
Ne Kazandım:Esneklik sağlandı; bir ürün hem garantili hem hediye paketli olabiliyor.
3. Adapter (Faz 2)
Nerede Kullanıldı: BankPaymentAdapter sınıfında.
Neden Kullanıldı: Kuruş bazlı çalışan dış bir banka kütüphanesini, TL bazlı çalışan sepetimize bağlamak için.
Ne Kazandım: Dış sisteme dokunmadan entegrasyon sağlandı.