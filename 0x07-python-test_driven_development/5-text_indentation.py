#!/usr/bin/python3
"""
This is the module 5-text_indentation
It contains one function: text_indentation
"""


def text_indentation(text):
    """
    prints text with 2 new lines after these characters: '?', '.', and ':'
    """
    if type(text) is not str:
        raise TypeError('text must be a string')
    ch = 0
    for char in text:
        if ch == 0:
            if char == " ":
                continue
            else:
                print(char, end="")
                ch = 1
        else:
            if char == "?" or char == "." or char == ":":
                print(char)
                print("")
                ch = 0
            else:
                print(char, end="")
