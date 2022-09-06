#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import BaseModel
from sqlalchemy import Column, String, ForeignKey
Base = declarative_base()


class City(BaseModel(Base)):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    state_id = Column(String(128), nullable=False)
    name = Column(String(128), nullable=False, ForeignKey("states.id"))
