from fastapi import FastAPI
from storage import load_products

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Привет, сервер работает!"}

@app.get("/products")
def get_all_products():
    products = load_products()
    return products
@app.get("/products/expensive")
def get_expensive_products(min_price: float):
    products = load_products()
    result = []
    for product in products:
        if product["price"] > min_price:
            result.append(product)
    return result