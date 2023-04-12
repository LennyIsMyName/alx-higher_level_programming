#!/usr/bin/python3

"""
append a string at the end of a text file and
return the number of characters added
"""


def append_write(filename="", text=""):
    """
    appends string to a file.
    Args:
        filename (file): the file
        text (string): the string to add to the file

    Returns: the number of characters added
    """
    with open(filename, mode="a", encoding="utf-8") as myFile:
        """
        appends to the file. creates a new one if no such file exists.
        Args:
            filename (file): the file
            mode (mode): open mode
        Returns:
            number of characters added.
        """
        append = myFile.write(text)
        return append
