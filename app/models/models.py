from sqlalchemy import Column , Integer , String
from sqlalchemy.ext.hybrid import hybrid_property
from flask_bcrypt import generate_password_hash , check_password_hash

from app import db


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(150),  nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    h_password = Column('password' , String(150),  nullable=False)

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