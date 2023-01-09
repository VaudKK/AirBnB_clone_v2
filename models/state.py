#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
from models import storage
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    
    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship("City",back_populates="State",
                        cascade="all, delete",
                        passive_deletes=True)
    else:
        @property
        def cities(self):
            """
            cities property
            """
            city_list = []
            for _, val in storage.all().items():
                try:
                    if val.state_id == self.id:
                        city_list.append(val)
                except AttributeError:
                    pass
            return city_list
