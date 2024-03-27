# Data Validation:
# Modify an existing FastAPI route that accepts a path parameter for user_id to ensure that user_id is an integer and greater than zero.

from fastapi import FastAPI, Path

app = FastAPI()

@app.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., title="The ID of the user to retrieve", gt=0)):
    """
    Retrieve user information by user ID.
    The ... is a placeholder indicating that user_id is required.
    The title parameter provides a description for user_id.
    The gt=0 parameter ensures that user_id is greater than zero. If user_id is not provided or is not an integer greater than zero, FastAPI will return a validation error.
    """
    return {"user_id": user_id}
