from abc import ABC, abstractmethod

# 1. TEMEL ÜRÜN VE DECORATOR YAPISI (Faz 1 & 2)
class Product(ABC):
    def __init__(self, name: str, price: float):
        self.name = name
        self._price = price

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

# 2. STRATEGY PATTERN (Faz 3 - Yeni)
# İndirim mantığını sepetten ayırarak OCP sağlar.

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

class PercentageDiscount(DiscountStrategy):
    def __init__(self, percent: float):
        self.percent = percent
    def apply_discount(self, total: float) -> float:
        return total * (1 - self.percent / 100)

class FixedAmountDiscount(DiscountStrategy):
    def __init__(self, amount: float):
        self.amount = amount
    def apply_discount(self, total: float) -> float:
        return max(0, total - self.amount)

class NoDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total

# 3. OBSERVER PATTERN (Faz 3 - Yeni)
# Sepete ürün eklendiğinde diğer sistemleri haberdar eder.

class Observer(ABC):
    @abstractmethod
    def update(self, product: Product):
        pass

class StockManager(Observer):
    def update(self, product: Product):
        print(f">>> [STOK BİLGİSİ]: {product.name} için stok çıkışı hazırlandı.")

class MarketingSystem(Observer):
    def update(self, product: Product):
        print(f">>> [PAZARLAMA]: Müşteri {product.name} ile ilgileniyor, benzer ürünleri öner!")

# 4. GÜNCELLENMİŞ CART VE DİĞERLERİ
class Cart:
    def __init__(self):
        self.items = []
        self._observers = []
        self._discount_strategy = NoDiscount()

    def attach(self, observer: Observer):
        self._observers.append(observer)

    def set_discount_strategy(self, strategy: DiscountStrategy):
        # OCP: Yeni indirim türü eklemek için bu sınıfı değiştirmemize gerek yok!
        self._discount_strategy = strategy

    def add_item(self, product: Product):
        self.items.append(product)
        # Observer'ları bilgilendir
        for observer in self._observers:
            observer.update(product)

    def calculate_total(self) -> float:
        total = sum(item.price for item in self.items)
        # Stratejiyi uygula
        return self._discount_strategy.apply_discount(total)

    def print_receipt(self):
        print("\n" + "="*50)
        print(" FAZ 3: DAVRANIŞSAL ÖRÜNTÜLER VE FINAL SEPETİ ")
        print("="*50)
        for item in self.items:
            print(f"{item.get_details():<38} | {item.price:>7} TL")
        print("-" * 50)
        print(f"İndirimsiz Toplam: {sum(i.price for i in self.items):>27} TL")
        print(f"ÖDENECEK TUTAR: {self.calculate_total():>29} TL")
        print("="*50)

class ProductFactory:
    @staticmethod
    def create_product(category: str, name: str, price: float) -> Product:
        category = category.capitalize()
        if category == "Electronics":
            return Electronics(name, price)
        elif category == "Food":
            return Food(name, price)
        return Electronics(name, price) # Default

class ExternalBankAPI:
    def make_payment(self, amount_in_cents: int):
        print(f"Banka API: {amount_in_cents / 100} TL ödeme onaylandı.")

class BankPaymentAdapter:
    def __init__(self, api: ExternalBankAPI):
        self.api = api
    def process_payment(self, amount: float):
        self.api.make_payment(int(amount * 100))

if __name__ == "__main__":
    # 1. Sistemi Hazırla
    sepet = Cart()
    sepet.attach(StockManager())
    sepet.attach(MarketingSystem())

    # 2. Ürünleri Oluştur ve Süsle
    telefon = ProductFactory.create_product("Electronics", "iPhone 15", 50000)
    garantili_telefon = WarrantyDecorator(telefon)
    
    # 3. Sepete Ekle (Observer'lar burada tetiklenecek)
    print("--- Ürünler Ekleniyor ---")
    sepet.add_item(garantili_telefon)
    sepet.add_item(ProductFactory.create_product("Food", "Kahve", 150))

    # 4. İndirim Stratejisini Belirle (OCP Gösterimi)
    # İstediğimiz stratejiyi Cart koduna dokunmadan seçebiliriz.
    sepet.set_discount_strategy(PercentageDiscount(10)) # %10 İndirim
    
    # 5. Çıktı ve Ödeme
    sepet.print_receipt()
    
    banka_api = ExternalBankAPI()
    ödeme = BankPaymentAdapter(banka_api)
    ödeme.process_payment(sepet.calculate_total())