#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list
    elif idx == len(my_list) - 1:
        mylist.remove(my_list[len(my_list) - 1])
    else:
        del(my_list[idx])
    return my_list
    
'''
    for i in range(idx, len(my_list) - 1):
        my_list[idx] = my_list[idx + 1]
        idx += 1
'''
