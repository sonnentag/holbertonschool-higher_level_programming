#!/usr/bin/python3
"""base module"""
import json


class Base():
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """to_json_string"""
        jstr = []
        if list_dictionaries:
            jstr = json.dumps(list_dictionaries, sort_keys=True)
        return (jstr)

    @classmethod
    def save_to_file(cls, list_objs):
        """save_to_file"""
        jstr = []
        if list_objs:
            jstr = cls.to_json_string([obj.to_dictionary()
                                      for obj in list_objs])
        with open(cls.__name__ + '.json',
                  mode="w", encoding="utf-8") as myFile:
            json.dump(jstr, myFile)

    @staticmethod
    def from_json_string(json_string):
        """from_json_string"""
        rstr = []
        if json_string:
            rstr = json.loads(json_string)
        return (rstr)

    @classmethod
    def create(cls, **dictionary):
        """create"""
        if cls.__name__ == "Rectangle":
            retd = cls(1, 1)
        if cls.__name__ == "Square":
            retd = cls(1, 1)
        retd.update(**dictionary)
        return (retd)

    @classmethod
    def load_from_file(cls):
        """load_from_file"""
        j = []
        return (j)

    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv"""
        pass

    def load_from_file_csv(cls):
        """load_from_file_csv"""
        pass
