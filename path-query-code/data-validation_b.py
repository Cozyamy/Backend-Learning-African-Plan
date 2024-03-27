# Data Validation:
# Add validation to a query parameter start_date to ensure it is a valid date format.

from fastapi import FastAPI, Query
from datetime import datetime

app = FastAPI()

def is_valid_date(date_string):
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

@app.get("/items/")
async def read_items(start_date: str = Query(..., description="Start date in YYYY-MM-DD format")):
    """
    Retrieve items based on start date.
    """
    if not is_valid_date(start_date):
        raise ValueError("Invalid date format. Please provide the start date in YYYY-MM-DD format.")

    return {"start_date": start_date}
