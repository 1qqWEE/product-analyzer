class Product:
    def __init__(self, data):
        self.title = data.get("title", "Unknown")
        self.price = data.get("price", 0)
        self.rating = data.get("rating", 0)
        self.reviews = data.get("reviews", [])

    def average_rating(self):
        if not self.reviews:
            return 0
        total = sum(review["rating"] for review in self.reviews)
        return total / len(self.reviews)

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "rating": self.average_rating()
        }


def product_report(products_data):
    result = []

    for item in products_data:
        product = Product(item)
        rating = product.average_rating()

        if rating >= 4.5:
            result.append({
                "title": product.title,
                "price": product.price,
                "rating": rating,
                "cheap": product.price < 20
            })

    return result


def statistics(products):
    if not products:
        return {}

    how = len(products)
    total = 0
    mostex = products[0]
    mostch = products[0]

    for product in products:
        total = total + product["price"]
        if product["price"] > mostex["price"]:
            mostex = product
        if product["price"] < mostch["price"]:
            mostch = product

    total = round(total, 2)
    middle = round(total / how, 2)

    l = {
        "Количество": how,
        "Общую стоимость": total,
        "Среднюю цену": middle,
        "Самый дорогой товар": {
            "title": mostex["title"],
            "price": mostex["price"]
        },
        "Самый дешёвый товар": {
            "title": mostch["title"],
            "price": mostch["price"]
        }
    }
    return l