# Code Writing: Query Parameters
# Implement default values for the query parameters (category defaulting to 'all' and price_range defaulting to a specific range)

from typing import Annotated
from fastapi import FastAPI, Query 

app = FastAPI()
products_data = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1500},
    {"id": 2, "name": "Phone", "category": "Electronics", "price": 900}
]

@app.get("/products/")
async def get_products(
    category: Annotated[str, Query(default='all', description="Filter products by category")] = 'all',
    price_range: Annotated[str, Query(default='0-1000', description="Price range (format: 'min-max')")] = '0-1000',
):
    """
    Retrieve a list of products filtered by category and price range.
    """
    min_price, max_price = map(float, price_range.split('-'))

    filtered_products = [
        product for product in products_data
        if (category == 'all' or product["category"] == category) and min_price <= product["price"] <= max_price
    ]

    return filtered_products