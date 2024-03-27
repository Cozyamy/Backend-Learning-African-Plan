# Data Validation:
# Add validation to a query parameter start_date to ensure it is a valid date format.

from fastapi import FastAPI, Query

app = FastAPI()

@app.get("/items/")
async def read_items(
    start_date: str = Query(
        ...,
        description="The start date for retrieving items (format: YYYY-MM-DD)",
        regex=r"\d{4}-\d{2}-\d{2}",
        example="2023-01-15"
    )
):
    """
    Retrieve items based on start date.
    """
    return {"start_date": start_date}
