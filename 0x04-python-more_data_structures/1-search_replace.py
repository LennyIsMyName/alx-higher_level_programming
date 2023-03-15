#!/usr/bin/python3

def search_replace(my_list, search, replace):
    newList = list()
    for i in range(len(my_list)):
        if my_list[i] == search:
            newList.append(replace)
        else:
            newList.append(my_list[i])
    return newList
