#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DbStorage
import os


storage_type = os.getenv('HBNB_TYPE_STORAGE')
storage = None

if storage_type == 'db':
    storage = DbStorage()
    storage.reload()
else:
    storage = FileStorage()
    storage.reload()
