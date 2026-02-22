from fastapi import APIRouter, HTTPException
from schema import User, UserCreate
import json
import os
from datetime import datetime

router = APIRouter()

FILE_NAME = "users.txt"


# HELPER FUNCTIONS

def read_users():
    users = []
    if not os.path.exists(FILE_NAME):
        return users

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line:
                users.append(json.loads(line))
    return users


def write_users(users):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        for user in users:
            f.write(json.dumps(user) + "\n")


def get_next_id(users):
    if not users:
        return 1
    return max(u["id"] for u in users) + 1


# MAKE 6 ENDPOINTS GET POST GET ID PUT ID DELETE ID 

# IMPORTANT NOTE: MAKE SURE THAT /SEARCH IS  BEFORE THE PARAMETRIC ROUTES LIKE /{id}

@router.post("/", status_code=201)
def create_user(user: UserCreate):
    users = read_users()

    new_user = User(
        id=get_next_id(users),
        name=user.name,
        age=user.age,
        created_at=datetime.utcnow().isoformat()
    ).model_dump()

    users.append(new_user)
    write_users(users)
    return new_user


@router.get("/")
def get_all_users():
    return read_users()


@router.get("/search")
def search_users(q: str):
    users = read_users()
    q_lower = q.lower()
    return [u for u in users if q_lower in u["name"].lower()]


@router.get("/{id}")
def get_user_by_id(id: int):
    users = read_users()
    for u in users:
        if u["id"] == id:
            return u
    raise HTTPException(status_code=404, detail="User not found")


@router.put("/{id}")
def update_user(id: int, user: UserCreate):
    users = read_users()

    for u in users:
        if u["id"] == id:
            u["name"] = user.name
            u["age"] = user.age
            write_users(users)
            return u

    raise HTTPException(status_code=404, detail="User not found")


@router.delete("/{id}")
def delete_user(id: int):
    users = read_users()

    for i, u in enumerate(users):
        if u["id"] == id:
            users.pop(i)
            write_users(users)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")
