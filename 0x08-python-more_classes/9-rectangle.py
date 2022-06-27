#!/usr/bin/python3
"""Rectangle - defines a rectangle"""


class Rectangle():
    """Rectangle - defines a rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """The _init_ method defines the properties of Rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """The _str_ method print a Rectangle with #"""
        acum = ""
        if (self.width * self.height > 0):
            for x in range(self.height):
                acum += (str(self.print_symbol) * self.width) + "\n"
            acum = acum[:-1]
        return acum

    def __repr__(self):
        """The _repr_ method return a string of Rectangle instance"""
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """The _del_ method print a message when an instance is deleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @property
    def width(self):
        """Return property width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set property width"""
        if (type(value) is not int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Return property height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set property height"""
        if (type(value) is not int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """Return area of Rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of Rectangle"""
        if (self.width == 0 or self.height == 0):
            return 0
        return 2 * (self.width + self.height)

    def bigger_or_equal(rect_1, rect_2):
        """bigger_or_equal - return bigger rectangle"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """square - return a new rectangle with equal size"""
        return cls(size, size)
        