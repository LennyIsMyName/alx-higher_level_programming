#!/usr/bin/python3

""" the base of all classes """
import json


class Base:
    """ defining the init """
    __nb_objects = 0

    def __init__(self, id=None):
        """ handle the id """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return json representation of class """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json representation of classes to json files """
        name = cls.__name__+".json"
        li = []
        for item in list_objs:
            li.append(item.to_dictionary())
        with open(name, "w") as file:
            file.write(cls.to_json_string(li))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the json string """
        if json_string is None:
            return list()
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an instance with all attributes already set. """
        if cls.__name__ == 'Square':
            temp = cls(2)
        elif cls.__name__ == 'Rectangle':
            temp = cls(2, 3)

        if isinstance(temp, Base):
            temp.update(**dictionary)
            return temp
