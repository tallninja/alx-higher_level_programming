#!/usr/bin/python3
"""
models/rectangle.py - Rectangle
"""
from models.base import Base


class Rectangle(Base):
    """defines a rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """constructor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """width setter"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """height setter"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """x getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """x setter"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """y getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """y setter"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """calulates the area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """prints to stdout the layout of rectangle"""
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print((" " * self.__x) + ("#" * self.__width))

    def __str__(self):
        """string representation of rectangle object"""
        id = self.id
        x = self.__x
        y = self.__y
        width = self.__width
        height = self.__height
        return f"[Rectangle] ({id}) {x}/{y} - {width}/{height}"

    def update(self, *args, **kwargs):
        """updates the class"""
        if args is not None and len(args) > 0:
            if len(args) >= 1:
                if type(args[0]) is not int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
            if len(args) > 1:
                self.__width = args[1]
            if len(args) > 2:
                self.__height = args[2]
            if len(args) > 3:
                self.__x = args[3]
            if len(args) > 4:
                self.__y = args[4]
        else:
            for k, v in kwargs.items():
                if k == "id":
                    self.id = v
                if k == "width":
                    self.__width = v
                if k == "height":
                    self.__height = v
                if k == "x":
                    self.__x = v
                if k == "y":
                    self.__y = v

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""
        rect_dict = {
            "x": self.__x,
            "y": self.__y,
            "id": self.id,
            "height": self.__height,
            "width": self.__width
        }
        return rect_dict
