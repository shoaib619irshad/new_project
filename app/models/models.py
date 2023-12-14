from app import db
from sqlalchemy import Column , Integer , String


class User(db.Model):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    username = Column(String(150),  nullable=False)
    email = Column(String(150), unique=True, nullable=False)
    password = Column(String(150),  nullable=False)
    