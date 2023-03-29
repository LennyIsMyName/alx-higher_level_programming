#!/usr/bin/python3

""" size validation """

class Square:
    """ The square class """

    def __init__(self, size=0):
        """ init a new square class. 
        Args:
            size (int): size to validate.
            """

        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
