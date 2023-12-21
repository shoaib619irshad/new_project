from flask import request ,jsonify
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from app.models.models import Role, User
from app.services.auth import *
from app import jwt


@jwt.user_identity_loader
def user_identity_lookup(user):
   return user

class AuthView(MethodView):
    def __init__(self, model: User = None) -> None:
        self.model = model

        
    def post(self):
        if request.path == "/signup":
            username = request.json.get("username",None)
            email = request.json.get("email",None)
            password = request.json.get("password", None)
            role = request.json.get("role", Role.EMPLOYEE.value)
            if username is None or email is None or password is None:
                return jsonify(message="All fields are required") , 400
            is_role_validate = validate_role(role)
            if  not is_role_validate:
                return jsonify(message="Invalid Role"), 400
            try:
                user = create_user( 
                    model = self.model,
                    username = username,
                    email = email,
                    password = password,
                    role = role
                    )
                return jsonify(message="User Signup successfully")
            except IntegrityError:
                return jsonify(message="The email already exists")
        
        elif request.path == "/login":
            email = request.json.get("email" , None)
            password = request.json.get("password" , None)
            if email is None or password is None:
                return jsonify(message="Invalid Credentials") , 400
            user = get_user_by_email(email)
            if user and user.verify_password(password):
                access_token = create_token(email)
                return jsonify({"message":"User login successfully", "access_token":access_token,"user":user.email})
            
            return jsonify(message="Email or password doesn't match")