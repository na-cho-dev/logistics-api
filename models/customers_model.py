#!/usr/bin/env python3
"""
This module contains a Customer class for defining all attributes/methods
"""
from models.base_model import BaseModel
from sqlalchemy import Column, String
from models.base_model import Base


class CustomerModel(BaseModel, Base):
    """
    Model of a User object

    Attributes:
        firstname (str): First name of the user
        lastname (str): Last name of the user
        username (str): Username of the user
        email (str): Email of the user
        phone_number (str): Phone number of the user
    """
    __tablename__ = 'customers'

    first_name = Column(String(128), nullable=False)
    last_name = Column(String(128), nullable=False)
    username = Column(String(128), unique=True, nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    phone_number = Column(String(20), nullable=False)
