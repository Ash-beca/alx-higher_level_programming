#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Represent a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student."""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrieves dictionary representation of the Student.
           If attrs is a list of strings, represents only those attributes
           included in the list.
        """
        if (type(attrs) == list and
                all(type(el) == str for el in attrs)):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student """

        for i, j in json.items():
            setattr(self, i, j)
