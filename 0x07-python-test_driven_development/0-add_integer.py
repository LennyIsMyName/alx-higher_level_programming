#!/usr/bin/python3

"""A function that adds 2 integers"""

def add_integer(a, b=98):
    """ this function adds two integers

    args:
        a (int): the first integer
        b (int): the second integer 'default is 98'

    Returns:
        int: the sum of a and b
    """
    if not isinstance(a, (float,int)):
        raise TypeError("a must be an integer")
    elif not isinstance(b, (float,int)):
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)

    return a + b
