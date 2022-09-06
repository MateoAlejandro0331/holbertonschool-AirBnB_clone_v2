#!/usr/bin/python3
"""This module defines a class call db_storage"""
from ast import Delete
from os import getenv
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class DBStorage():
    """
    This module defines a class call db_storage
    """

    __engine = None
    __session = None

    def __init__(self):
        """Init method"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                        .format(getenv('HBNB_MYSQL_USER'),
                                                getenv('HBNB_MYSQL_PWD'),
                                                getenv('HBNB_MYSQL_HOST'),
                                                getenv('HBNB_MYSQL_DB')),
                                        pool_pre_ping=True)
        Base.metadata.create_all(self.__engine)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """Return a dictionary called FileStorage"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        types_of_objects = (User, State, City, Amenity, Place, Review)
        if (cls == None):
            self.__engine = types_of_objects
    
    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Nothing for now"""
        pass


