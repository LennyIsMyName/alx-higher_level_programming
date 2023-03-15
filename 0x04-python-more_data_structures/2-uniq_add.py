#!/usr/bin/python3

def uniq_add(my_list=[]):
    ans = 0
    for num in my_list:
        if my_list.count(num) > 1:
            my_list.remove(num)
    for i in my_list:
        ans = ans + i
    return ans
