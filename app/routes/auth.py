from flask import Blueprint

from app.views import AuthView
from app.models import User

auth_bp = Blueprint('auth', __name__)

auth_bp.add_url_rule(
    rule='/signup',
    view_func=AuthView.as_view(
        "signup",
        model=User,
    )
)

auth_bp.add_url_rule(
    rule='/login',
    view_func=AuthView.as_view(
        "login",
        model=User
    )
)