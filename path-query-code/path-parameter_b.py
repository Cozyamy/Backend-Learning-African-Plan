# Code Writing: Path Parameters
# Implement error handling for the case when the user_id path parameter is missing.

from fastapi import FastAPI, HTTPException

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
        raise HTTPException(status_code=404, detail="User not found")
    return users[user_id]
