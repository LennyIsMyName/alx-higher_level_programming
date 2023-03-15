#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    li = sorted(list(a_dictionary.keys()))
    newdict = dict()
    for i in li:
        newdict[i] = a_dictionary[i]
    
    for key, value in newdict.items():
        print(key, end=': ')
        print(value)
