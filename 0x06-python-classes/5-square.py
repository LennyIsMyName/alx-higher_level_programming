#!/usr/bin/python3

""" size validation of Square"""

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
    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value


    def area(self):
        """ returns the area of the current square"""
        var = self.__size * self.__size
        return var

    def my_print(self):
        """ prints a square of # characters """
        if self.__size:
            for i in range(self.__size):
                for j in range(self.__size):
                    print('#', end='') 
                print()
        elif self.__size == 0:
            print()
