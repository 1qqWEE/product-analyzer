from api import get_products
from analysis import product_report, statistics
from storage import save_products, load_products

products = get_products()

report_products = product_report(products)


save_products(report_products)

stats = statistics(load_products())

if stats:
    print(stats)
    print(stats["Среднюю цену"])
    print(stats["Самый дорогой товар"]["title"])
else:
    print("Отчёт пуст или не найден")