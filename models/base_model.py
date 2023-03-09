#!/usr/bin/python3

import uuid
from datetime import datetime
import models


class BaseModel:
    """ defines all common attributes/methods for other classes"""

    def __init__(self, id, *args, **kwargs):

        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)
        else:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    v = datetime.strptime(v, "%Y-%m-%dT%H:%M:%S.%f")
                if k != "__class__":
                    setattr(self, k, v)

    def __str__(self):
        """returns class name, id and attribute dictionary"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """updates last update time"""
        self.updated_at = datetime.now()
        storage.save(self)

    def to_dict(self):
        """returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        conv = self.__dict__.copy()
        conv["created_at"] = self.created_at.isoformat()
        conv["updated_at"] = self.updated_at.isoformat()
        conv["__class__"] = self.__class__.__name__
        return conv
