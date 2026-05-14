Faz 1: Creational (Yaratımsal) Örüntüler
1. Factory Method
Nerede Kullanıldı: src/cart.py içerisindeki ProductFactory sınıfı ve Cart.add_item metodu içerisinde kullanıldı.  
Neden Kullanıldı: Faz 0'da sepet sınıfı (Cart), hangi ürünün nasıl yaratılacağını (if-else bloklarıyla) kendisi biliyordu. Bu durum "God Class" sorununa ve esneklik kaybına yol açıyordu. Nesne yaratma sorumluluğunu sepetten ayırmak için bu örüntü seçildi. 
 Ne Kazandım:Loose Coupling (Gevşek Bağlılık): Sepet artık somut ürün sınıflarına (Electronics, Food) doğrudan bağımlı değil.  
  OCP Desteği: Yeni bir ürün kategorisi eklemek için sepetin kodunu değiştirmeye gerek kalmadı; sadece fabrikaya yeni bir seçenek eklemek yeterli.  
  Single Responsibility: Sepet sadece ürünleri listelemeye, fabrika ise sadece ürünleri üretmeye odaklandı.
FAZ 0
classDiagram
    class ProductFactory {
        +static create_product(category)
    }
    class Product { <<abstract>> }
    ProductFactory --> Product : creates
    Product <|-- Electronics
    Product <|-- Food
   
FAZ 1
   classDiagram
    class ProductFactory {
        +create_product(category, name, price) Product$
    }
    
    class Product {
        <<abstract>>
        +name: str
        +price: float
        +get_details()*
    }
    
    class Electronics {
        +get_details()
    }
    
    class Food {
        +get_details()
    }

    ProductFactory ..> Product : "creates"
    Product <|-- Electronics
    Product <|-- Food

    note for ProductFactory "Nesne yaratma sorumluluğu\nburada merkezileştirilmiştir."
   
