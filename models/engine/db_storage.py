#!/usr/bin/python3
"""This module defines a class call db_storage"""
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import (create_engine)
from models.base_model import BaseModel, Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class DBStorage:
    """
    This module defines a class call db_storage
    """

    __engine = None
    __session = None
    classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                }

    def __init__(self):
        """Init method"""
        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}/{}'.format(
                getenv('HBNB_MYSQL_USER'), getenv('HBNB_MYSQL_PWD'),
                getenv('HBNB_MYSQL_HOST'), getenv('HBNB_MYSQL_DB')),
            pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Return a dictionary called FileStorage"""
        mydic = {}
        if (cls is None):
            for input_class in DBStorage.classes:
                query = self.__session.query(input_class).all()
                for instance in query:
                    mydic[f"{instance.__class__}.{instance.id}"] = instance
        else:
            query = self.__session.query(cls).all()
            for instance in query:
                mydic[f"{instance.__class__}.{instance.id}"] = instance
        return(mydic)

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
        """create all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session1 = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(Session1)
        self.__session = Session()

    def close(self):
        """close method"""
        self.__session.close()
