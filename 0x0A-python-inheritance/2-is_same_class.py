#!/usr/bin/python3
""" is_same_class module """


def is_same_class(obj, a_class):
    """ returns True if object is an instance of the specified class """
    return type(obj) is a_class
