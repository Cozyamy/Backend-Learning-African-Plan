# Code Writing: Path Parameters
# Write a FastAPI route that accepts a path parameter for user identification (user_id) and returns the user's profile information.

from fastapi import FastAPI

app = FastAPI()
users = {
    1: {"username": "Cozyamy", "email": "cozy@example.com"},
    2: {"username": "Haybee", "email": "haybee@example.com"}
}

@app.get("/users/{user_id}")
async def get_user_profile(user_id: int):
    """
    Retrieve the profile information of a user by user_id.
    """
    if user_id not in users:
        return {"error": "User not found"}
    return users[user_id]
