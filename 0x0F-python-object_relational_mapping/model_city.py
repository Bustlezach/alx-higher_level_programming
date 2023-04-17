#!/usr/bin/python3
"""
This script defines a State class and
a Base class to work with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    """State class

    Attributes:
        __tablename__ (str): The table name of the class
        id (int): The State id of the class
        name (str): The State name of the class

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey('states.id')

