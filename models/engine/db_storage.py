#!/usr/bin/python3
'''
The db storage module
'''

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class DbStorage():

    __engine = None
    __session = None

    def __init__(self) -> None:
        env = os.getenv('HBNB_ENV')
        user_name = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        self.__engine = create_engine(f'mysql://{user_name}:{passwd}@{host}/{db}', pool_pre_ping = True)
        session_factory = sessionmaker(bind=self.__engine,expire_on_commit=False)
        Session = scoped_session(session_factory)
        
        if env == 'test':
            Base.metadata.drop_all(bind=self.__engine)
        
        self.__session = Session()

    def all(self, cls=None):
        """Get records either all or based on class name"""
        result = []
        if cls != None:
            for instance in self.__session.query(cls):
                result.append({instance.to_dict()['__class__'] + '.' + instance.id: instance})
        else:
            classes = {
                        'User': User, 'Place': Place,
                        'State': State, 'City': City, 'Amenity': Amenity,
                        'Review': Review
                        }
            
            for _, value in classes:
                for instance in self.__session.query(value):
                    result.append({instance.to_dict()['__class__'] + '.' + instance.id: instance})
            
            return result
        
    
    def new(self, obj):
        """Insert a new record to the database"""
        self.__session.add(obj)
    
    def save(self):
        """commit changes to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete object"""
        if obj != None:
            self.__session(obj)
    
    def reload(self):
        from base_model import Base
        Base.metadata.create_all(self.__engine)