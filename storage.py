import json

def save_report(report):
    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, ensure_ascii=False, indent=4)

def load_report():
    with open("report.json", "r", encoding="utf-8") as file:
        stats = json.load(file)
    return stats