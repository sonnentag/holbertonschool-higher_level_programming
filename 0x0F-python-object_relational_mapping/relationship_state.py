#!/usr/bin/python3
""" the class definition of a State and an instance Base """

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class State(Base):
    ''' State '''

    __tablename__ = 'states'

    id = Column(Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)

    name = Column(String(128), nullable=False)
    cities = relationship('City', cascade='all, delete', backref='state')