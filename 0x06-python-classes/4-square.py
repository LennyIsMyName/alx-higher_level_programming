#!/usr/bin/python3

""" Area of a square """

class Square:
    def __init__(self, size=0):
        """ instances size. 
        Args:
            size (int): size to validate.
            """
        self.__size = size

    try:
        def check_type(self):
            if isinstance(self.__size, int):
                if (self.__size < 0):
                    raise ValueError("size must be >= 0")
            else:
                raise TypeError("size must be an integer")
    except TypeError as t:
        t = "size must be an integer"
        print(t)
    except ValueError as v:
            v = "size must be >= 0"
            print(v)
    def area(self):
        """ returns the square of a number """
        area = self.__size**2
        return (area)
    @property
    def size(self):
        return self.__size
    @size.setter
    def size(self, size):
        self.__size = size
