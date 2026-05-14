from abc import ABC, abstractmethod

# 1. TEMEL ÜRÜN YAPISI (Faz 1'den)
class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price # Decorator'lar için korumalı hale getirdik

    @property
    def price(self) -> float:
        return self._price

    @abstractmethod
    def get_details(self) -> str:
        pass

class Electronics(Product):
    def get_details(self):
        return f"[Elektronik] {self.name}"

class Food(Product):
    def get_details(self):
        return f"[Gıda] {self.name}"

# 2. DECORATOR ÖRÜNTÜSÜ (Faz 2 - Yeni)
# Ürünlere kodlarını değiştirmeden dinamik özellik eklememizi sağlar.

class ProductDecorator(Product):

    def __init__(self, wrapped_product: Product):
        self._product = wrapped_product
        super().__init__(wrapped_product.name, wrapped_product.price)

class GiftWrapDecorator(ProductDecorator):
    def get_details(self):
        return self._product.get_details() + " + [Hediye Paketi]"

    @property
    def price(self):
        return self._product.price + 15.0

class WarrantyDecorator(ProductDecorator):
    def get_details(self):
        return self._product.get_details() + " + [1 Yıl Ek Garanti]"

    @property
    def price(self):
        return self._product.price + 100.0

# 3. ADAPTER ÖRÜNTÜSÜ (Faz 2 - Yeni)
# Dış sistemleri (Banka API vb.) kendi sistemimize uyumlu hale getirir.

# Varsayılan dış kütüphane (Değiştiremediğimiz kod)
class ExternalBankAPI:
    def make_payment(self, amount_in_cents: int):
        # Bu API kuruş cinsinden tam sayı bekliyor
        print(f"Banka API: {amount_in_cents / 100} TL ödeme başarıyla alındı.")

# Bizim sistemimizin beklediği arayüz
class PaymentProcessor(ABC):
    @abstractmethod
    def process_payment(self, amount: float):
        pass

class BankPaymentAdapter(PaymentProcessor):
    def __init__(self, api: ExternalBankAPI):
        self.api = api

    def process_payment(self, amount: float):
        # TL'yi kuruşa çevirip dış API'ye gönderiyoruz
        cents = int(amount * 100)
        self.api.make_payment(cents)

# 4. YARATIM VE YÖNETİM (Geliştirilmiş)
class ProductFactory:
    @staticmethod
    def create_product(category: str, name: str, price: float) -> Product:
        category = category.capitalize()
        if category == "Electronics":
            return Electronics(name, price)
        elif category == "Food":
            return Food(name, price)
        raise ValueError("Geçersiz kategori!")

class Cart:
    def __init__(self):
        self.items = []
        self.discount_code = None

    def add_item(self, product: Product):
        self.items.append(product)

    def calculate_total(self) -> float:
        total = sum(item.price for item in self.items)
        if self.discount_code == "YILBASI":
            total *= 0.80
        return max(0, total)

    def print_receipt(self):
        print("\n" + "="*45)
        print(" FAZ 2: STRUCTURAL PATTERNS SEPETİ ")
        print("="*45)
        for item in self.items:
            print(f"{item.get_details():<35} | {item.price:>7} TL")
        print("-" * 45)
        print(f"TOPLAM: {self.calculate_total():>32} TL")
        print("="*45)


if __name__ == "__main__":
    # 1. Ürünü Factory ile oluştur
    laptop = ProductFactory.create_product("Electronics", "Gaming Laptop", 25000)
    
    # 2. Ürünü Decorator'lar ile süsle (Dinamik özellik ekleme)
    # Laptop + Garanti + Hediye Paketi
    decorated_laptop = WarrantyDecorator(laptop)
    decorated_laptop = GiftWrapDecorator(decorated_laptop)
    
    # 3. Sepete ekle ve yazdır
    sepet = Cart()
    sepet.add_item(decorated_laptop)
    sepet.add_item(ProductFactory.create_product("Food", "Çikolata", 20))
    
    sepet.print_receipt()

    # 4. Adapter kullanarak dış banka sistemiyle ödeme yap
    banka_servisi = ExternalBankAPI()
    ödeme_aracı = BankPaymentAdapter(banka_servisi)
    
    toplam = sepet.calculate_total()
    print(f"\nÖdeme işlemi başlatılıyor: {toplam} TL")
    ödeme_aracı.process_payment(toplam)