#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
import os

# Import City for FileStorage
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        # For DBStorage: relationship with the class City
        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan"
                              )
    else:
        @property
        def cities(self):
            """FileStorage relationship between State and City."""
            city_list = []
            for city in models.storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
