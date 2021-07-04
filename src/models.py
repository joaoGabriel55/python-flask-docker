from sqlalchemy import Column, Integer, String
from src.database import Base


class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    age = Column(Integer())

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"{self.name}:{self.age}"
