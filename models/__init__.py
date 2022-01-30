#!/usr/bin/python3
"""
Init files for models package
Creare variable storage an instance of filestorage
"""

from models.engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
