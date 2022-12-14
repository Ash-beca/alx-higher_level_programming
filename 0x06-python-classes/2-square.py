#!/usr/bin/python3
''' A Module that creates a Square object '''

class Square;
''' Creating an Object template '''

    def __init__(self, size = 0):
        """Method to initialize the square object"""
            if not isinstance(size, int):
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = int(size)
