#!/usr/bin/python3
''' add_item function '''

import sys
import json
from os import path
""" add the object as json"""
to = __import__('5-save_to_json_file').save_to_json_file

""" get the json object """
fro = __import__('6-load_from_json_file').load_from_json_file


def add_item(args: list[str]):
    """
    add, load and then save to a file 
    """
    file = "add_item.json"

    if path.isfile(file):
        """ get the json object """
        li = fro(file)
    else:
        li = []
    li.extend(args)
    """ append the list to json file as json """
    to(li, file)


if __name__ == '__main__':
    add_item(sys.argv[1:])
