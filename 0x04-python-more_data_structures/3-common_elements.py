#!/usr/bin/python3

def common_elements(set_1, set_2):
    li = list()
    for el in set_1:
        if el in set_2:
            li.append(el)
    return set(li)
