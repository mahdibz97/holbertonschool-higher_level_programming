#!/usr/bin/python3
"""Define class base"""


import json


class Base:
    """manage id attribute"""
    __nb_objects = 0

    def __init__(self, id=None):
        """init"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation of list_dictionaries"""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return '[]'
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file"""
        file = cls.__name__ + ".json"
        with open(file, "w") as f:
            li = []
            if list_objs is not None:
                li = [item.to_dictionary() for item in list_objs]
            f.write(Base.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """Update the class Base by adding the static method"""
        if json_string is None:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            rec = cls(5, 5)
        else:
            rec = cls(5)
        rec.update(**dictionary)
        return rec

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        try:
            with open(cls.__name__+'.json', encoding='utf-8') as File:
                line = File.read()
                object = cls.from_json_string(line)
                list = []
                for i in object:
                    list.append(cls.create(**i))
                return list
        except FileNotFoundError:
            return []
