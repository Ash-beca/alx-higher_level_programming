#!/usr/bin/python3
"""Defines a text file-reading function."""


def read_file(filename=""):
    """Print the contents of a UTF8 text file to stdout."""

    with open(filename, encoding="utf-8") as my_file_0:
        print(my_file_0.read(), end="")
