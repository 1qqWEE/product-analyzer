def safe_product_info(product):
    cc = {
        "title": product.get("title", "Unknown"),
        "price": product.get("price", 0),
        "rating": product.get("rating", 0)
    }
    return cc

def average_rating(product):
    total = 0
    count = 0
    mid = 0
    for review in product["reviews"]:
        count = count + 1
        total = total + review["rating"]
        mid = total / count
    return mid

def clean_products(products):
    cleaned = []
    for product in products:
        cleaned.append(safe_product_info(product))
    return cleaned

def product_report(products):
    result = []
    for product in products:
        rating = average_rating(product)
        if rating >= 4.5:
            result.append({
                "title": product["title"],
                "price": product["price"],
                "rating": rating,
                "cheap": product["price"] < 20
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