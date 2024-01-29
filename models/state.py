#!/usr/bin/python3
""" State Module for HBNB project """

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


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
        name = ""

    @property
    def cities(self):
        """
        Returns the list of City instances
        with state_id equals to the current State.id
        """
        from models import storage
        from models.city import City
        city_list = []
        for city in storage.all(City).values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list
