#!/usr/bin/python3
"""
Moule base_model
This class defines
all common attributes/methods
for other classes
"""

import models
from uuid import uuid4
from datetime import datetime

class BaseModel:
    """
    Defines attributes required by base model
    Attributes
       __init__(self, *args, **kwargs)
       __str__(self)
       __save(self)
       to_dict(self)
    """
    
    def __init__(self, *args, **kwargs):
        """
        Handles initialization of base model
        takesargs and kwargs
        id should be uuid of typr str
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at":
                    self.created_at = datetime.strptime(
                        kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "updated_at":
                    self.updated_at = datetime.strptime(
                        kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
                elif key == "__class__":
                    continue
                else:
                    self.__dict__[key] = value
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid4())
            models.storage.new(self)

    def __str__(self):
        """Returns string representation of base model"""

        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """update attribute updated_at with current datetime"""

        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Returns dictionary representation of key/values of the instance"""

        x_dict = self.__dict__copy()
        x_dict["created_at"] = self.created_at.isoformat()
        x_dict["updated_at"] = self.updated_at.isoformat()
        x_dict["__class__"] = self.__class__.name__
        return x_dict
    
