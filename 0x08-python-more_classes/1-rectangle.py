#!/usr/bin/python3
""" defines class rectangle """


class Rectangle:
    """ rectangle with private instance attributes width and height """

    def __init__(self, width=0, height=0):
        """
        initializes rectangle

        """
        
        self.height = height
        self.width = width

    @property
    def width(self):
        """ finds the private attribute width """
        return self.__width

    @width.setter
    def width(self, value):
        """ validates width as a positive integer """
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """ finds the attribute height """
        return self.__height

    @height.setter
    def height(self, value):
        """ validates height as a positive integer """
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
