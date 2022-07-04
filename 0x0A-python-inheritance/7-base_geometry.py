#!/usr/bin/python3

"""
class BaseGeometry - base geometry
"""


class BaseGeometry:
    """base geometry class"""

    def area(self):
        """calculates the area"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
