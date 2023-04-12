#!/usr/bin/python3

import os


""" opens a file and print it to stdout """


def read_file(filename=""):
    """
    Reads the filename
    Args:
        filename (file): the file object to read.

    Returns:
        nothing
    """
    with open(filename, encoding="utf-8") as myFile:
        """
        opens the filename object with utf-8 encoding
        Args:
            filename (file): the file object passed
            encoding (encode): encode type
        Returns:
            nothing
        """
        print(myFile.read())
