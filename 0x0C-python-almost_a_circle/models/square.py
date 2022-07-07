#!/usr/bin/python3
"""
models/square.py - Square
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square from a rectangle"""

    def __init__(self, size, x=0, y=0):
        """constructor"""
        super().__init__(width=size, height=size, x=x, y=y)

    def __str__(self):
        """string representation of a square"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
