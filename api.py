import requests


def get_products():
    try:
        response = requests.get("https://dummyjson.com/products")
        response.raise_for_status()

        data = response.json()

        return data.get("products", [])

    except requests.RequestException as e:
        print(f"Ошибка при запросе к API: {e}")
        return []