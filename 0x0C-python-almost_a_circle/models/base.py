#!/usr/bin/python3

"""Defines a base model class."""
import json
import turtle


class Base:
    """Represent the base model for this module """

    __nb_objects = 0

    def __init__(self, id=None):
       
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
       """returns the JSON string representation of list_dictionaries"""
       
       if list_dictionaries is None or list_dictionaries == []:

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Write the JSON serialization of a list of objects to a file."""

        filename = cls.__name__ + ".json"
        with open(filename, "w") as myfile:
            if list_objs is None:
                myfile.write("[]")
            else:
                list_dicts = [obj.to_dictionary() for obj in list_objs]
                myfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return the deserialization of a JSON string."""

        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Return a class instantied from a dictionary of attributes that is already set."""

        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(2, 8, 5, 10)
            elif cls.__name__ == "Square":
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Return a list of all instances. """

        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as myfile:
                list_dicts = Base.from_json_string(myfile.read())
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

   

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw Rectangles and Squares using the turtle module."""

        ob = turtle.Turtle()
        ob.screen.bgcolor("#35378b")
        ob.pensize(4)
        ob.shape("turtle")

        ob.color("#f5f5f5")
        for rect in list_rectangles:
            ob.showturtle()
            ob.up()
            ob.goto(rect.x, rect.y)
            ob.down()
            for i in range(2):
                ob.forward(rect.width)
                ob.left(90)
                ob.forward(rect.height)
                ob.left(90)
            ob.hideturtle()

        ob.color("#00ffff")
        for sq in list_squares:
            ob.showturtle()
            ob.up()
            ob.goto(sq.x, sq.y)
            ob.down()
            for i in range(2):
                ob.forward(sq.width)
                ob.left(90)
                ob.forward(sq.height)
                ob.left(90)
            ob.hideturtle()

        turtle.exitonclick()
