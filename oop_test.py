class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items
    
    def total_price(self):
        total = 0
        for item in self.items:
            total = total + item["price"]
        return total
        
    
    def show_receipt(self):
        print(f"Заказ для: {self.customer_name}")
        for item in self.items:
            print(f"{item['title']}: {item['price']}")
        print(f"Итого: {self.total_price()}") 
alisher_order = Order("Алишер", [
    {"title": "Яблоко", "price": 2},
    {"title": "Банан", "price": 1}
])
alisher_order.show_receipt()
