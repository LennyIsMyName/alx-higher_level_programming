#!/usr/bin/python3

""" A function that inserts a line of text to a file, after every line that contains a specific string """

def append_after(filename="", search_string="", new_string=""):
    """ imputs a string in the next line after a specific string """
    emptyStr = list()
    with open(filename, "r", encoding="utf-8") as f:
        """ reads the filename line by line """
        for line in f:
            if line.find(search_string) != -1:
                emptyStr.append(line)
                emptyStr.append(new_string)
                continue
            emptyStr.append(line)

    with open(filename, mode="w", encoding="utf-8") as file:
        """ writes the new mutated object """
        for i in emptyStr:
            file.write(i)
