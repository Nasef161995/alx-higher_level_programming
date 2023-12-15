#!/usr/bin/python3
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class MyTable(Base):
    __tablename__ = 'my_table'
    id = Column(Integer, primary_key=True)
    name = Column(String(255))
    age = Column(Integer)

m = MyTable()
