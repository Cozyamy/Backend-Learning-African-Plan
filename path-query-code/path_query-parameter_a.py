# Combining Path and Query Parameters:
# Write a FastAPI route that accepts a path parameter for city (city_id) and query parameters for filtering restaurants by cuisine type (cuisine) and rating (min_rating).


from typing import Annotated
from fastapi import FastAPI, Query

app = FastAPI()

restaurants = [
    {"id": 1, "name": "Restaurant A", "city_id": 1, "cuisine": "Italian", "rating": 4.5},
    {"id": 2, "name": "Restaurant B", "city_id": 1, "cuisine": "Mexican", "rating": 4.2}
]

@app.get("/restaurants/{city_id}")
async def get_restaurants(
    city_id: int,
    cuisine: Annotated[str | None, Query(description="Filter restaurants by cuisine type")] = None,
    min_rating: Annotated[float | None, Query(description="Filter restaurants by minimum rating")] = None,
):
    """
    Retrieve a list of restaurants in a city filtered by cuisine type and minimum rating.
    """
    filtered_restaurants = [
        restaurant for restaurant in restaurants
        if restaurant["city_id"] == city_id
        and (cuisine is None or restaurant["cuisine"].lower() == cuisine.lower())
        and (min_rating is None or restaurant["rating"] >= min_rating)
    ]

    return filtered_restaurants

