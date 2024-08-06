"""Model users Definition"""
from sqlalchemy import Column, Integer, String

from app.repo.database import Base


class Users(Base):
    """Users model"""
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    password = Column(String)
