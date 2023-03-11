#!/usr/bin/python3
"""Base model for our console."""
import datetime
import uuid
import models


class BaseModel:
    """Represent the Base model of the program."""

    def __init__(self, *args, **kwargs):
        """Initialize instances."""
        if len(args) > 0:
            for k in args[0]:
                setattr(self, k, args[0][k])
        else:
            self.created_at = datetime.datetime.now()
            self.id = str(uuid.uuid4())
        for k in kwargs:
            print("kwargs: {}: {}".format(k, kwargs[k]))

    def save(self):
        """Update self."""
        self.updated_at = datetime.datetime.now()
        models.storage.new(self)
        models.storage.save()

    def __str__(self):
        """Define string representation."""
        return "[{}] ({}) {}".format(type(self)
                                     .__name__, self.id, self.__dict__)

    def to_dict(self):
        """Serialize objects."""
        dupe = self.__dict__.copy()
        dupe["created_at"] = str(dupe["created_at"])
        if "updated_at" in dupe:
            dupe["updated_at"] = str(dupe["updated_at"])
        dupe["__class__"] = type(self).__name__
        return dupe
