#!/usr/bin/python3

"""Defines a file-writing function."""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file"""

    with open(filename, "w", encoding="utf-8") as file:
        file.write(text)
        no_of_char = len(text)
        file.close()
        print(no_of_char)
    
