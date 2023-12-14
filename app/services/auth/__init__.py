from app import db
from typing import Any

def create_user(model: Any, id: str, username: str, email: str, password: str):
    user = model(
        id = id,
        username = username,
        email = email,
        password=password,
    )
    db.session.add(user)
    db.session.commit()

    return user
