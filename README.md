Esnek ve Genişletilebilir E-Ticaret Sepeti Sistemi
📌 Proje Seçimi ve Gerekçesi
Seçilen Konu: D - E-Ticaret Sepeti Sistemi

Gerekçe: E-ticaret sistemleri; yapısal ve davranışsal tasarım örüntülerinin (Decorator, Strategy, Observer) gerçek dünya senaryolarına en iyi şekilde uygulanabileceği dinamik bir yapıya sahiptir. Bu projeyi, nesne yönelimli programlama prensiplerini ve sistemin genişletilebilirliğini (Open/Closed Principle) en somut şekilde deneyimlemek için seçtim.

Projenin Amacı ve Özellikleri
Bu proje, yazılım tasarım prensipleri (SOLID) kullanılarak geliştirilmiş esnek bir sepet yönetim sistemidir. Temel işlevler şunlardır:

Factory Method ile farklı kategorilerde (Elektronik, Gıda vb.) ürün oluşturma.

Decorator ile ürünlere çalışma anında hediye paketi veya ek garanti ekleme.

Strategy ile sepet kodunu değiştirmeden farklı indirim mantıkları uygulama.

Observer ile sepet hareketlerini stok ve pazarlama birimlerine otomatik bildirme.

Adapter ile dış ödeme sistemleri (Banka API) ile uyumlu çalışma.

Kullanılan Tasarım Örüntüleri
| Faz | Örüntü | Açıklama |
| :--- | :--- | :--- |
|Faz 1|Factory Method| Nesne yaratma mantığını merkezileştirerek `Cart` sınıfının somut ürün sınıflarına olan bağımlılığını ortadan kaldırdık. |
|Faz 2|Decorator| Ürün sınıflarına dokunmadan, çalışma anında (runtime) ürünlere ek maliyet ve özellik (Garanti, Hediye Paketi) ekledik. |
|Faz 2|Adapter| Sistemimizin beklediği TL formatını, dış Banka API'sinin beklediği kuruş formatına dönüştürerek uyumluluk sağladık. |
|Faz 3|Strategy| İndirim mantığını sepetten soyutlayarak, yeni indirim türlerinin sepet kodunu değiştirmeden eklenebilmesini (OCP) sağladık. |
|Faz 3|Observer| Sepete ürün eklendiğinde Stok ve Pazarlama birimlerinin olay tabanlı (event-driven) olarak haberdar olmasını sağladık. |

classDiagram
    class Product {
        <<abstract>>
        +name: str
        +price: float
        +get_details()*
    }
    
    class Electronics { +get_details() }
    class Food { +get_details() }

    class ProductDecorator {
        <<abstract>>
        -wrapped_product: Product
        +get_details()*
    }

    class GiftWrapDecorator { +get_details() }
    class WarrantyDecorator { +get_details() }

    class DiscountStrategy {
        <<abstract>>
        +apply_discount(total)*
    }

    class PercentageDiscount { +apply_discount(total) }
    class NoDiscount { +apply_discount(total) }

    class Observer {
        <<interface>>
        +update(product)*
    }

    class StockManager { +update(product) }
    class MarketingSystem { +update(product) }

    class BankPaymentAdapter {
        -api: ExternalBankAPI
        +process_payment(amount)
    }

    Product <|-- Electronics
    Product <|-- Food
    Product <|-- ProductDecorator
    ProductDecorator *-- Product : "wraps"
    
    Cart o-- Product : "contains"
    Cart --> DiscountStrategy : "uses"
    Cart --> Observer : "notifies"
    
    DiscountStrategy <|-- PercentageDiscount
    Observer <|.. StockManager
    
    BankPaymentAdapter --> ExternalBankAPI : "adapts"

Nasıl Çalıştırılır?
Bu projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

1. Ön Hazırlık
Sisteminizde Python 3.10 veya daha güncel bir sürümün yüklü olduğundan emin olun. Kurulu olup olmadığını kontrol etmek için:

python --versioN

2. Projeyi İndirme (Clone)
Terminal veya PowerShell üzerinden depoyu klonlayın:

git clone https://github.com/sanemunl/mini-sepet-projesi.git
cd mini-sepet-projesi

3. Uygulamayı Çalıştırma
Projenin ana mantığını ve tasarım örüntülerinin çıktısını görmek için sepet dosyasını çalıştırın:

python src/cart.py

4. Test ve Çıktı
Uygulama çalıştığında terminalde şunları göreceksiniz:

Ürünlerin fabrika (Factory) tarafından oluşturulması.

Decorator'lar ile eklenen özellikler ve fiyat güncellemeleri.

Observer sinyalleri (Stok ve Pazarlama bildirimleri).

Adapter aracılığıyla yapılan simüle edilmiş banka ödemesi.