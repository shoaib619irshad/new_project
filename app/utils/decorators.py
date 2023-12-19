from functools import wraps

from flask import jsonify
from flask_jwt_extended import get_current_user, jwt_required

from app import jwt
from app.services.auth import get_user_by_email


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header , jwt_data):
   identity = jwt_data["sub"]
   user = get_user_by_email(identity)
   if user is None:
       return None
   return user


def adm_mgr_required(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        current_user = get_current_user()
        role = current_user.role.value
        if role == "employee":
            return jsonify(message="You are not Authorized"), 401
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        current_user = get_current_user()
        role = current_user.role.value
        if role != "admin":
            return jsonify(message="You are not Authorized"), 401
        return f(*args, **kwargs)
    return decorated_function