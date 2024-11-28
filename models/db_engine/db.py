#!/usr/bin/env python3
"""
Database Module
"""
from os import getenv
from flask_sqlalchemy import SQLAlchemy
from models.base_model import Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage():
    """
    Defines the databse storage
    """
    __engine = None
    __session = None

    def __init__(self) -> None:
        """
        Initialize the database engine
        and link it to the MySQL Database
        """
        db_env = getenv('DB_ENV')
        db_username = getenv('DB_USERNAME')
        db_password = getenv('DB_PASSWORD')
        db_host = getenv('DB_HOST')
        db_port = getenv('DB_PORT')
        db_name = getenv('DB_NAME')

        db_url = f"mysql+mysqldb://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}"

        self.__engine = create_engine(db_url)
        # Base.metadata.drop_all(self.__engine)

        if db_env == 'test':
            Base.metadata.drop_all(self.__engine)

    def test_connection(self):
        from models.customers_model import CustomerModel
        """
        Test the database connection by querying a sample table
        """
        try:
            result = self.__session.query(CustomerModel).all()
            return result  # Returns all user records
        except Exception as e:
            return f"Error: {e}"

    def all(self, cls):
        """
        Query on the current database session and return a dictionary
        """
        if cls is None:
            classes = Base.__subclasses__()
        else:
            classes = [cls]
        
        result = {}
        for clss in classes:
            objects = self.__session.query(clss).all()
            for obj in objects:
                key = f"{obj.__class__.__name__}.{obj.id}"
                result[key] = obj
        return result
    
    def create(self, obj):
        """
        Adds an object to the current database session
        """
        self.__session.add(obj)

    def save(self):
        """
        Commits all changes of the current database session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        Deletes obj from the current database session
        """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """
        Creates all tables in the database
        """
        Base.metadata.create_all(self.__engine)

        """
        self.__session = scoped_session(sessionmaker(
            bind=self.__engine, expire_on_commit=False))
        """
        session_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def close(self):
        """
        Closes the session
        """
        self.__session.remove()

    def query(self, cls):
        """
        Helper method for querying the database
        """
        return self.__session.query(cls)

    def get(self, cls, id):
        """
        A method to retrieve one object
        Args:
            cls - Class
            id - String representing the object ID
        """
        result = self.__session.query(cls).filter_by(id=id).first()
        return result
