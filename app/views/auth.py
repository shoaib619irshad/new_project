from flask import request ,jsonify
from flask.views import MethodView
from sqlalchemy.exc import IntegrityError

from app.models.models import User
from app.services.auth import *

class AuthView(MethodView):
    def __init__(self, model: User = None) -> None:
        self.model = model

        
    def post(self):
        if request.path == "/signup":
            id = request.json.get("id",None)
            username = request.json.get("username",None)
            email = request.json.get("email",None)
            password = request.json.get("password", None)
            task_id = request.json.get("task_id",None)
            if id is None or username is None or email is None or password is None:
                return jsonify(message="Invalid Credentials") , 400
            try:
                user = create_user( 
                    model = self.model,
                    id = id,
                    username = username,
                    email = email,
                    password = password,
                    task_id = task_id
                    )
                return jsonify(message="User Signup successfully")
            except IntegrityError:
                return jsonify(message="The id or email already exists or task_id not found")
        
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