from api import get_products
from analysis import product_report, statistics
from storage import save_report, load_report

products = get_products()

report_products = product_report(products)
stats = statistics(report_products)

save_report(stats)

stats = load_report()

if stats:
    print(stats)
    print(stats["Среднюю цену"])
    print(stats["Самый дорогой товар"]["title"])
else:
    print("Отчёт пуст или не найден")