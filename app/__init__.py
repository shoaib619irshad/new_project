import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager

from app.config import config

db = SQLAlchemy()
jwt = JWTManager()

def create_app(config_name):
    app = Flask(__name__)
    
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)

    db.init_app(app)
    jwt.init_app(app)

    from app.routes.auth import auth_bp
    from app.routes.tasks import tasks_bp
    from app.routes.task_assign import task_assign_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(tasks_bp)
    app.register_blueprint(task_assign_bp)

    return app


config_name = os.getenv('CONFIG', 'default')

app = create_app(config_name)