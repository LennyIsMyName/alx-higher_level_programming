#!/usr/bin/python3

def max_integer(my_list=[]):
    biggy = my_list[0]
    for i in range(1, len(my_list)):
        if my_list[i] > biggy:
            biggy = my_list[i]
    return biggy
