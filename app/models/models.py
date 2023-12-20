from enum import Enum

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import generate_password_hash, check_password_hash

from app import db

class Role(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    EMPLOYEE = "employee"

class Status(Enum):
    UNASSIGNED = "unassigned"
    RUNNING = "running"
    PENDING = "pending"
    COMPLETED = "completed"

class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(150),  nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    h_password = Column('password' , String(150),  nullable=False)
    role = Column(db.Enum(Role), nullable=False)

    @hybrid_property
    def password(self):
        return self.h_password 
    
    @password.setter
    def password(self, simple_password):
        self.h_password = generate_password_hash(simple_password)

    def verify_password(self, simple_password):
        return check_password_hash(self.h_password, simple_password)

    def __repr__(self) -> str:
        return '<User %r>' % self.email
    

class Tasks(db.Model):
    __tablename__ = 'tasks'

    id = Column(Integer , primary_key=True)
    title = Column(String(150) , nullable=False)
    description = Column(String(500) , nullable=True)
    status = Column(db.Enum(Status), nullable=False)
    assigned_to = Column(Integer, ForeignKey("user.id"))