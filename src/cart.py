class Cart:
    def __init__(self):
        self.items = []
        self.discount_code = None

    def add_item(self, name, price, category):
        self.items.append({"name": name, "price": price, "category": category})

    def calculate_total(self):
        total = sum(item["price"] for item in self.items)
        
        # KÖTÜ TASARIM: İndirim mantığı sepetin içine gömülü (if-else zinciri)
        if self.discount_code == "YILBASI":
            total *= 0.80  # %20 indirim
        elif self.discount_code == "OGRENCI":
            total -= 10    # 10 TL sabit indirim
        elif self.discount_code == "KUPON20":
            total -= 20
        
        return total

    def print_receipt(self):
        print("--- SEPET DETAYI ---")
        for item in self.items:
            print(f"{item['name']} - {item['price']} TL")
        print(f"Toplam: {self.calculate_total()} TL")