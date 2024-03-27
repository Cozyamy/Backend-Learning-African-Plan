# Usage and Benefits:
# Analyze a given FastAPI application and identify instances where using path parameters would be more appropriate than query parameters, and vice versa.
# Discuss the benefits of using path and query parameters in the provided FastAPI application and how it enhances API design.

from fastapi import FastAPI, Query
from typing import Annotated

app = FastAPI()

products = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1500},
    {"id": 2, "name": "Phone", "category": "Electronics", "price": 900},
]

orders = [
    {"id": 1, "product_id": 1, "quantity": 2, "status": "pending"},
    {"id": 2, "product_id": 2, "quantity": 1, "status": "completed"}
]

@app.get("/products/{product_id}")
async def get_product(product_id: int):
    """
    Retrieve product information by product ID.
    """
    for product in products:
        if product["id"] == product_id:
            return product
    return {"error": "Product not found"}

@app.get("/orders/")
async def get_orders(
    product_id: int,
    status: Annotated[str | None, Query(description="Filter orders by status")] = None
):
    """
    Retrieve orders by a specific product with optional status filter.
    """
    orders_by_product = [order for order in orders if order["product_id"] == product_id]
    if status:
        orders_by_product = [order for order in orders_by_product if order["status"] == status]
    return orders_by_product


# Path Parameters:
# Use: Path parameters are used in the route "/products/{product_id}" to retrieve product information by a specific product ID.
# Benefit: Adding the product_id directly into the URL path, this identifies the resource (product) requested. It ensures that the endpoint retrieves the correct product information based on the provided ID.

# Query Parameters:
# Use: Query parameters are used in the route "/orders/" to filter orders by a specific product and an optional status.
# Benefit: Query parameters provide a flexible way to modify the results returned by an endpoint without altering the URL structure. The product_id parameter serves as a mandatory filter criterion to fetch orders associated with a particular product. Clients can customize the response based on their specific requirements without filling up the URL path.

# Using a combination of path and query parameters enhances API design by providing a well-structured, flexible, and intuitive interface for clients to interact with the API