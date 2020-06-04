#!/usr/bin/python3
"""13-student"""


class Student:
    """Student class"""

    def __init__(self, first_name, last_name, age):
        """student class init"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """to_json"""

        attribs = {}
        if attrs is not None and type(attrs) is list:
            for attr in attrs:
                if type(attr) == str and attr in self.__dict__:
                    attribs[attr] = self.__dict__.get(attr)
            return (attribs)

        return (self.__dict__)

    def reload_from_json(self, json):
        """reload_from_json"""

        for k, v in json.items():
            self.__dict__.update({k: v})
