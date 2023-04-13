#!/usr/bin/python3
"""save obj to json file as json"""
import json

"""save obj to json file as json"""


def save_to_json_file(my_obj, filename):
    """save obj to json file as json"""
    with open(filename, "w") as file:
        """write it to the file"""
        json.dump(my_obj, file)
