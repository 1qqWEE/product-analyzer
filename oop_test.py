class Product:
    def __init__(self, title, price):
        self.title = title
        self.price = price

    def show_info(self):
        print(f"{self.title} стоит {self.price} долларов")


apple = Product("Яблоко", 2)
apple.show_info()
banana = Product("Банан", 1)
banana.show_info()