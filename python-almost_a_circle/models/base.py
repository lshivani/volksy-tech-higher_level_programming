#!/usr/bin/python3
"""base Module"""
import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializer for Base class"""
        if id is not None:
            self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Returns the JSON string representation of a
        list of dictionaries.
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        if type(list_dictionaries) != list:
            raise TypeError("list_dictionaries must be a list of dictionaries")
        for dic in list_dictionaries:
            if type(dic) is not dict:
                err = "list_dictionaries must be a list of dictionaries"
                raise TypeError(err)
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Writes the JSON string representation of a
        list of instances to a file
        """
        filename = cls.__name__ + ".json"
        dicList = []
        if list_objs is not None:
            for obj in list_objs:
                dicList.append(obj.to_dictionary())

        with open(filename, mode='w', encoding='utf-8') as f:
            f.write(cls.to_json_string(dicList))
