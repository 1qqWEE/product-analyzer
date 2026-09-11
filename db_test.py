import sqlite3

connection = sqlite3.connect("shop.db")
cursor = connection.cursor()

cursor.execute("UPDATE products SET price = ? WHERE title = ?", (3, "Яблоко"))

connection.commit()
connection.close()

print("Изменено")