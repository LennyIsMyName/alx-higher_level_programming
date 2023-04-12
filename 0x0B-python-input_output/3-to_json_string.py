#!/usr/bin/python3

import json


""" JSON representation of an object """


def to_json_string(my_obj):
    """
    converts an object to JSON
    Args:
        my_obj (object): the object to be converted.
    Returns: the JSON representation of my_obj
    """
    return json.dumps(my_obj)
