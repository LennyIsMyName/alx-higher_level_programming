#!/usr/bin/python3
""" get all attributes and methods available """
def lookup(obj):
    """
    Returns a list of all available methods and attributes of an object.
    
    Args:
        obj (obj): the object.

    Returns:
        list: list of all attributes and methods
    """
    return dir(obj)
