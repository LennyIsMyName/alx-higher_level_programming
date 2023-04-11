#!/usr/bin/python3

""" This program checks whether an object is an instance of a class """
def is_same_class(obj, a_class):
    """
    Returns true if obj is an instance of a_class.

    Args:
        obj (object): The object
        a_class (class): the class.

    Returns:
        True if isinstance or False
        """
    return type(obj) == a_class
