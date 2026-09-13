import sqlite3

def save_products(products):
    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            price REAL,
            rating REAL
        )
    """)

    cursor.execute("DELETE FROM products")

    for product in products:
        cursor.execute(
            "INSERT INTO products (title, price, rating) VALUES (?, ?, ?)",
            (product["title"], product["price"], product["rating"])
        )

    connection.commit()
    connection.close()


def load_products():
    connection = sqlite3.connect("shop.db")
    cursor = connection.cursor()

    cursor.execute("SELECT title, price, rating FROM products")
    rows = cursor.fetchall()

    connection.close()

    products = []
    for row in rows:
        products.append({
            "title": row[0],
            "price": row[1],
            "rating": row[2]
        })

    return products