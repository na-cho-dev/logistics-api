#!/usr/bin/env python3
"""
This module contains a Product class defining all attributes/methods
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship


class OrderModel(BaseModel, Base):
    """
    Model of a User object

    Attributes:
        firstname (str): First name of the user
        lastname (str): Last name of the user
        username (str): Username of the user
        email (str): Email of the user
        phone_number (str): Phone number of the user
    """
    __tablename__ = 'orders'


    customer_id = Column(String(60), ForeignKey('customers.id'), nullable=False)
    order_name = Column(String(128), nullable=False)
    order_description = Column(Text, nullable=False)
    order_purchase_time = Column(DateTime, nullable=False)
