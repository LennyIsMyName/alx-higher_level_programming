#!/usr/bin/python3
def remove_char_at(str, n):
    newStr =''
    i = 0
    length = len(str)
    while i < length:
        if i == n:
            continue
        newStr = newStr + str[i]
    return newStr
