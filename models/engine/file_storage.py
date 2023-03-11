#!/usr/bin/python3
"""File storage module."""
import json
from datetime import datetime
from models import *


class FileStorage:
    """Storage for objects created."""

    __file_path = "file.json"
    __objects = {}

    def __init__(self):
        """Initialize instances."""
        self.reload()

    def all(self):
        """Display all objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Create new object."""
        if obj is not None:
            FileStorage.__objects[obj.id] = obj

    def save(self):
        """Save a new instance."""
        store = {}
        for k in FileStorage.__objects.keys():
            store[k] = FileStorage.__objects[k].to_dict()

        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as fd:
            fd.write(json.dumps(store))

    def reload(self):
        """Refresh objects."""
        try:
            with open(FileStorage.__file_path,
                      mode="r+", encoding="utf-8") as fd:
                FileStorage.__objects = {}
                temp = json.load(fd)
                for k in temp.keys():
                    cls = temp[k].pop("__class__", None)
                    cr_at = temp[k]["created_at"]
                    cr_at = datetime.strptime(cr_at, "%Y-%m-%d %H:%M:%S.%f")
                    up_at = temp[k]["updated_at"]
                    up_at = datetime.strptime(up_at, "%Y-%m-%d %H:%M:%S.%f")
                    FileStorage.__objects[k] = eval(cls)(temp[k])
        except Exception as e:
            pass
