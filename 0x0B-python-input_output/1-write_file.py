#!/usr/bin/python3

""" this program writes text into a file """

def write_file(filename="", text=""):
    """
    writes into filename file
    Args:
        filename (file): the file
        text (str): the text to add to the file.
    Returns:
        the number of characters added into the file.
    """
    with open(filename, mode="w") as myFile:
        """
        This opens a file obect to write to.
        Args:
            filename (file): the file.
            mode (mode): the mode of opening the file.
            text (str): the text to add to the file.
        Returns:
            number of chars input.
        """
        return myFile.write(text)

