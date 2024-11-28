#!/usr/bin/env python3
"""Create a storage instance for the application"""
from models.db_engine.db import DBStorage
from models.customers_model import CustomerModel


storage = DBStorage()
storage.reload()
