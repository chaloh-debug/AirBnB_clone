#!/usr/bin/python3
"""creates intances of storage object"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
