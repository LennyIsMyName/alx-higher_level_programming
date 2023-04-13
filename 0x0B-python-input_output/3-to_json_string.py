#!/usr/bin/python3

import json


""" JSON representation of an object """


def to_json_string(my_obj):
    """ converts an object to JSON """
    jsn = json.dumps(my_obj)
    return jsn
