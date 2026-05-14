class Cart:
    def __init__(self):
        # Ürünler nesne olarak değil, basit birer sözlük (dict) olarak tutuluyor.
        # Bu durum veri bütünlüğü ve esneklik sorunlarına yol açar.
        self.items = [] 
        self.discount_code = None

    def add_item(self, name, price, category):
      
        self.items.append({
            "name": name, 
            "price": price, 
            "category": category
        })

    def calculate_total(self):
       
        total = sum(item["price"] for item in self.items)
        
        # İndirim hesaplamaları if-else zincirleri ile yapılıyor.
        if self.discount_code == "YILBASI":
            total *= 0.80  # %20 indirim
        elif self.discount_code == "OGRENCI":
            total -= 10    # 10 TL sabit indirim
        elif self.discount_code == "KUPON20":
            total -= 20
        elif self.discount_code == "CUMA":
            total *= 0.70  # %30 indirim
        
        return total

    def print_receipt(self):
       
        print("\n--- FAZ 0: KÖTÜ TASARIM SEPET FİŞİ ---")
        for item in self.items:
            # Ürün tipleri arasında davranış farkı sadece if blokları ile ayrılıyor.
            type_label = ""
            if item["category"] == "Elektronik":
                type_label = "[ELK]"
            elif item["category"] == "Gıda":
                type_label = "[GIDA]"
            
            print(f"{type_label} {item['name']} - {item['price']} TL")
            
        print(f"Uygulanan Kod: {self.discount_code if self.discount_code else 'Yok'}")
        print(f"Toplam Ödenecek: {self.calculate_total()} TL")

if __name__ == "__main__":
    my_cart = Cart()
    my_cart.add_item("Laptop", 20000, "Elektronik")
    my_cart.add_item("Elma", 50, "Gıda")
    
    my_cart.discount_code = "YILBASI"
    my_cart.print_receipt()