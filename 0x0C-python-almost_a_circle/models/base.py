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

    def to_json_string(list_dictionaries):
        """to_json_string"""
        jstr = []
        if list_dictionaries:
            jstr = json.dumps(list_dictionaries, sort_keys=True)

        return (jstr)

    def save_to_file(cls, list_objs):
        """save_to_file"""
        pass

    def from_json_string(json_string):
        """from_json_string"""
        pass

    def create(cls, **dictionary):
        """create"""
        pass

    def load_from_file(cls):
        """load_from_file"""
        pass

    def save_to_file_csv(cls, list_objs):
        """save_to_file_csv"""
        pass

    def load_from_file_csv(cls):
        """load_from_file_csv"""
        pass
