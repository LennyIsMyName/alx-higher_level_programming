#!/usr/bin/python3
""" return obj from json file"""
import json


def load_from_json_file(filename):
    """ return obj from json file"""
    with open(filename, mode="r", encoding="utf-8") as file:
        """ return obj from json file"""
        obj = json.load(file)
        return obj
