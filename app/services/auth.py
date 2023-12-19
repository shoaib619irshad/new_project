import datetime , os

from flask_jwt_extended import create_access_token
from typing import Any

from app import db
from app.models.models import User

def create_user(model: Any, id: int, username: str, email: str, password: str, task_id: str):
    user = model(
        id = id,
        username = username,
        email = email,
        password=password,
        task_id = task_id
    )
    db.session.add(user)
    db.session.commit()

    return user

def get_user_by_email(email):
    user = User.query.filter_by(email=email).first()
    return user

def create_token(email):
    expires = datetime.timedelta(days=int(os.getenv('DAYS')))
    access_token = create_access_token(identity=email, expires_delta=expires)
    return access_token