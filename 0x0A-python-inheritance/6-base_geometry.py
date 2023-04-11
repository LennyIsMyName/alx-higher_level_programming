#!/usr/bin/python3

""" this program creates an empty class """


class BaseGeometry():
    """
    creates an empty class
    improvement.. raise exception
    """
    def area(self):
        """
        just raise an exception
        """
        raise Exception("area() is not implemented")
