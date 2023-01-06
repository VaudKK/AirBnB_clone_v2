#!/usr/bin/python3
'''
The db storage module
'''

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbStorage():

    def __init__(self) -> None:
        env = os.getenv('HBNB_ENV')
        user_name = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')

        Session = sessionmaker(bind=self.__engine)
        self.__engine = create_engine(f'mysql://{user_name}:{passwd}@{host}/{db}')
        self.__session = Session()

    def all(self, cls):
        pass
