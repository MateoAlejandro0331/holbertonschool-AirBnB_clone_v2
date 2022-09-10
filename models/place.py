#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship
import models


# metadata = Base.metadata

# place_amenity = Table('association', metadata,
#    Column('place_id', String(60), ForeignKey('places.id'), primary_key=True, nullable=False),
#    Column('amenity_id', String(60), ForeignKey('amenities.id'), primary_key=True, nullable=False)
#)

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    if getenv("HBNB_TYPE_STORAGE") == 'db':
        city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
        user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship('Review', cascade='all, delete', backref='place')
        # amenities = relationship('Amenity', backref='places', secondary='place_amenity', viewonly=False)
    else:
        # getter method
        def reviews(self):
            list_ins = []
            for review in models.storage.all(models.review):
                if review.place_id == self.id:
                    list_ins = review
            return list_ins
