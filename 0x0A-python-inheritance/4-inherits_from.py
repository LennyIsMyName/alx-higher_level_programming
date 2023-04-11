#!/usr/bin/python3

""" This program checks whether an class is a subclass of another class """


def inherits_from(obj, a_class):
    """
    Returns true if obj is a subclass of a_class.

    Args:
        obj (object): The object
        a_class (class): the class.

    Returns:
        True if isinstance or False
    """
    return issubclass(type(obj), a_class)
