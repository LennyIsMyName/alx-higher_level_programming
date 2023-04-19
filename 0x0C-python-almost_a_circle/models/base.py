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

    def to_json_string(list_dictionaries):
        """ return json representation of class """
        if list_dictionaries == None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
