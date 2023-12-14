from flask.views import MethodView
from flask import request ,jsonify
from app.models.models import User
from app.services.auth import create_user

class AuthView(MethodView):
    def __init__(self, model: User = None) -> None:
        self.model = model

        
    def post(self):
        data = request.json
        user = create_user( 
            model = self.model,
            id = data["id"],
            username = data["username"],
            email = data["email"],
            password = data["password"]
            )
        return jsonify({"message":"User Signup successfully"})