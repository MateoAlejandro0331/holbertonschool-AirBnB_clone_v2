#!/usr/bin/python3
"""This module defines a class call db_storage"""
from os import getenv
from sqlalchemy.orm import scoped_session, sessionmaker, Session
from sqlalchemy import (create_engine)
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from sqlalchemy import Column, String, ForeignKey

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
        types_of_objects = [User, State, City, Amenity, Place, Review]
        self.__session = Session(self.__engine)
        if (cls == None):
            query = self.__session.query(User, State, City, Amenity, Place, Review).all()
            for instance in query:
                print(f"All method cls=None {instance} finish all method")
        else:
            query = self.__session.query(cls).all()
            for instance in query:
                print(f"All method {instance} finish all method")
    
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
        my_session = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(my_session)
        self.__session = Session()


        



