# Code Writing: Query Parameters
# Create a FastAPI route that accepts query parameters for filtering a list of products by category and price range.

from typing import Annotated
from fastapi import FastAPI, Query 

app = FastAPI()
products_data = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 150000},
    {"id": 2, "name": "Phone", "category": "Electronics", "price": 90000}
]

@app.get("/products/")
async def get_products(
    category_filter: Annotated[str | None, Query(description="Filter products by category")] = None,
    price_range_filter: Annotated[str | None, Query(description="Price range (format: 'min-max')")] = None,
):
    """
    Retrieve a list of products filtered by category and price range.
    """
    filtered_products = products_data

    if category_filter:
        filtered_products = [product for product in filtered_products if product["category"] == category_filter]

    if price_range_filter is not None:
        min_price, max_price = map(float, price_range_filter.split('-'))
        filtered_products = [product for product in filtered_products if min_price <= product["price"] <= max_price]

    return filtered_products
