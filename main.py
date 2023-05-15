from typing import Optional, List
from fastapi import FastAPI, Path, Query
from pydantic import BaseModel

description = """
fast-api API tutorial. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
"""

app = FastAPI(
    title="fast-api-msr",
    description=description,
    version="0.0.1",
    terms_of_service="http://example.com/terms/",
    contact={
        "name": "msr",
        "url": "http://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "MIT",
    },
)

users = []


class User(BaseModel):
    email: str
    is_active: bool
    bio: Optional[str]


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/users")
async def create_user(user: User):
    users.append(user)
    return "Success"


@app.get("/users/{id}")
async def get_user(
    id: int = Path(..., description="The id of the user ...", gt=2),
    q: str = Query(None, max_length=5),
):
    return {"user": users[id], "query": q}
