#!/usr/bin/python3
""" the class definition of a city """

from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base, State


class City(Base):
    ''' City '''

    __tablename__ = 'cities'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)

    name = Column(String(128), nullable=False)

    state_id = Column(Integer, ForeignKey(State.id), nullable=False)
