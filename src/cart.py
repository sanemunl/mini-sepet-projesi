from abc import ABC, abstractmethod
# 1. SOYUT ÜRÜN SINIFI (Abstract Base Class)
# Önceki fazdaki sözlük (dict) yapısından nesne tabanlı yapıya geçiş.
class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    @abstractmethod
    def get_details(self) -> str:
        pass

# 2. SOMUT ÜRÜN SINIFLARI (Concrete Products)
class Electronics(Product):
    def get_details(self):
        return f"[Elektronik] {self.name}: {self.price} TL"

class Food(Product):
    def get_details(self):
        return f"[Gıda] {self.name}: {self.price} TL"

class Clothing(Product):
    def get_details(self):
        return f"[Giyim] {self.name}: {self.price} TL"

# 3. FACTORY METHOD ÖRÜNTÜSÜ (Creational)
# Nesne yaratma sorumluluğu Cart sınıfından merkezi bir fabrikaya taşındı.
class ProductFactory:
    @staticmethod
    def create_product(category: str, name: str, price: float) -> Product:
        category = category.strip().capitalize()
        if category == "Electronics":
            return Electronics(name, price)
        elif category == "Food":
            return Food(name, price)
        elif category == "Clothing":
            return Clothing(name, price)
        else:
            # Bilinmeyen kategoriler için genel bir ürün döndürülür veya hata fırlatılır.
            # Ödev gereği esneklik için temel Product sınıfı döndürülebilir.
            class GeneralProduct(Product):
                def get_details(self): return f"[Genel] {self.name}: {self.price} TL"
            return GeneralProduct(name, price)

# 4. GÜNCELLENMİŞ SEPET SINIFI (Refactored Cart)
class Cart:
    def __init__(self):
        self.items = [] # Artık içinde sözlük değil, Product nesneleri tutar.
        self.discount_code = None

    def add_item(self, category: str, name: str, price: float):
      
        product = ProductFactory.create_product(category, name, price)
        self.items.append(product)

    def calculate_total(self) -> float:
        total = sum(item.price for item in self.items)
        
        # NOT: İndirim mantığı Faz 3'te Strategy Pattern ile tamamen temizlenecek.
        if self.discount_code == "YILBASI":
            total *= 0.80
        elif self.discount_code == "OGRENCI":
            total -= 10
            
        return max(0, total) # Fiyatın negatif çıkmaması için

    def print_receipt(self):
        print("\n" + "="*35)
        print(" FAZ 1: FACTORY METHOD SEPETİ ")
        print("="*35)
        
        if not self.items:
            print("Sepetiniz boş.")
        else:
            for item in self.items:
                # Polymorphism: Nesne tipine göre doğru get_details() çağrılır.
                print(item.get_details())
        
        print("-" * 35)
        print(f"Uygulanan İndirim: {self.discount_code if self.discount_code else 'Yok'}")
        print(f"Toplam Ödenecek: {self.calculate_total():.2f} TL")
        print("="*35)

if __name__ == "__main__":
    sepet = Cart()
    
    # Ürünler kategori ismiyle ekleniyor
    sepet.add_item("Electronics", "Akıllı Saat", 4500)
    sepet.add_item("Food", "Organik Bal", 250)
    sepet.add_item("Clothing", "Yün Kazak", 850)
    
    sepet.discount_code = "YILBASI"
    sepet.print_receipt()