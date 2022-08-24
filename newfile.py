from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

from sqlalchemy.ext.declarative import declarative_base

Base1 = declarative_base()
engine = create_engine("sqlite:///test2.db", echo=True)


class Student(Base1):
    __tablename__ = "student"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)




