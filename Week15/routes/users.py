from fastapi import APIRouter, HTTPException
from datetime import datetime

from schema import UserCreate
from user_store import UserStore

router = APIRouter()

# Week 15: SQLite database file
store = UserStore("users.db")


def get_next_id(users):
    if not users:
        return 1
    return max(u["id"] for u in users) + 1


# IMPORTANT: /search BEFORE /{id}

@router.get("/")
def get_all_users():
    return store.load()


@router.post("/", status_code=201)
def create_user(user: UserCreate):
    users = store.load()
    new_user = {
        "id": get_next_id(users),
        "name": user.name,
        "age": user.age,
        "created_at": datetime.utcnow().isoformat(),
    }
    # Save just this one user
    store.save([new_user])
    return new_user


@router.get("/search")
def search_users(q: str):
    users = store.load()
    q_lower = q.lower()
    return [u for u in users if q_lower in u["name"].lower()]


@router.get("/{id}")
def get_user_by_id(id: int):
    u = store.find_by_id(id)
    if u is None:
        raise HTTPException(status_code=404, detail="User not found")
    return u


@router.put("/{id}")
def update_user(id: int, updated: UserCreate):
    success = store.update_user(id, {"name": updated.name, "age": updated.age})
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return store.find_by_id(id)


@router.delete("/{id}")
def delete_user(id: int):
    success = store.delete_user(id)
    if not success:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted"}