#!/usr/bin/python3

""" size validation """

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
    except TypeError:
        def geterr():
            return "size must be an integer"
        geterr()
    except ValueError:
        def geterr():
            return "size must be >= 0"
        geterr()
