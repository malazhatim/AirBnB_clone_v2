#!/usr/bin/python3
"""This is the user class"""
from models.base_model import BaseModel, Base
from os import getenv
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """ Represent a user for a MySQL database """

    __tablename__ = "users"

    if getenv('HBNB_TYPE_STORAGE') == 'db':
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
