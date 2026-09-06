class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items
    
    def total_price(self):
        total = 0
        for item in self.items:
            total = total + item.get("price", 0)
        return total
        
    
    def show_receipt(self):
        print(f"Заказ для: {self.customer_name}")
        for item in self.items:
            print(f"{item.get('title', None)}: {item.get('price', 0)}")
        print(f"Итого: {self.total_price()}") 
broken_order = Order("Тест", [{"title": "Штука без цены"}])
broken_order.show_receipt()
