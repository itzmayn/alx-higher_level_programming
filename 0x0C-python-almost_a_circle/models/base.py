#!/usr/bin/python3
"""

A model that contains a Base class to manage
the id attribute of all classes that extend
from Base and avoid duplicating the same code.

"""

from os import path
import json


class Base:
    """
    Base class to manage id attribute and file I/O operations
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a Base instance with an id
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Converts a list of dictionaries to a JSON string
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Saves a list of objects to a file in JSON format
        """
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for obj in list_objs:
                json_attrs.append(obj.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """
        Converts a JSON string to a list of dictionaries
        """
        if json_string is None or len(json_string) == 0:
            return []

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Creates a new instance of the class using a dictionary of attributes
        """
        if cls.__name__ == 'Square':
            dummy = cls(3)

        if cls.__name__ == 'Rectangle':
            dummy = cls(3, 3)

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Loads a list of instances from a file
        """
        filename = cls.__name__ + '.json'

        if not path.exists(filename):
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for obj in objs:
                instances.append(cls.create(**obj))

            return instances
