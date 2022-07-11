#!/usr/bin/python3
"""
A module that test differents behaviors
of the Base class
"""
import unittest
import os
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBase(unittest.TestCase):
    """
    A class to test the Base Class
    """
    def test_id_as_positive(self):
        """
        Test for a positive Base Class id
        """
        base_instance = Base(115)
        self.assertEqual(base_instance.id, 115)
        base_instance = Base(67)
        self.assertEqual(base_instance.id, 67)

    def test_id_as_negative(self):
        """
        Test for a negative Base Class id
        """
        base_instance = Base(-91)
        self.assertEqual(base_instance.id, -91)
        base_instance = Base(-4)
        self.assertEqual(base_instance.id, -4)

    def test_id_as_none(self):
        """
        Test for a None Base Class id
        """
        base_instance = Base()
        self.assertEqual(base_instance.id, 1)
        base_instance = Base(None)
        self.assertEqual(base_instance.id, 2)

    def test_string_id(self):
        with self.assertRaises(TypeError) as msg:
            warn = Base('Monty Python')
        self.assertEqual("id must be an integer", str(msg.exception))

    def test_to_json_string(self):
        """
        Test the to_json_string method
        """
        rect_instance = Rectangle(10, 7, 2, 8, 70)
        rect_data = re1.to_dictionary()
        json_data = Base.to_json_string([rect_data])
        self.assertEqual(type(json_data), str)

    def test_empty_to_json_string(self):
        """
        Test for a empty data on the to_json_string method
        """
        empty_data = []
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

        empty_data = None
        json_data = Base.to_json_string(empty_data)
        self.assertEqual(json_data, "[]")

    def test_instance(self):
        """
        Test a Base Class instance
        """
        base_instance = Base()
        self.assertEqual(type(base_instance), Base)
        self.assertTrue(isinstance(base_instance, Base))

    def test_to_json_string(self):
        """
        Test a normal to_json_string functionality
        """
        rect_data = {'id': 31, 'x': 14, 'y': 11, 'width': 3, 'height': 3}
        json_data = Base.to_json_string([rect_data])

        self.assertTrue(isinstance(rect_data, dict))
        self.assertTrue(isinstance(json_data, str))
        self.assertCountEqual(
            json_data,
            '{["id": 31, "x": 14, "y": 11, "width": 3, "height": 3]}'
        )

    def test_wrong_to_json_string(self):
        """
        Test a wrong functionality of the
        to_json_string method
        """
        json_data = Base.to_json_string(None)
        self.assertEqual(json_data, "[]")

        warn = ("Base.to_json_string() missing 1 required positional argument: " +
                "'list_dictionaries'")

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string()

        self.assertEqual(warn, str(msg.exception))

        warn = "Base.to_json_string() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Base.to_json_string([{43, 87}], [{22, 17}])

        self.assertEqual(warn, str(msg.exception))

    def test_wrong_save_to_file(self):
        """
        Test the save_to_file method
        """
        with self.assertRaises(AttributeError) as msg:
            Base.save_to_file([Base(1), Base(2)])

        self.assertEqual(
             "'Base' object has no attribute 'to_dictionary'",
             str(msg.exception)
        )

    def test_load_from_file(self):
        """
        Test the load_from_file method
        """
        if os.path.exists("Base.json"):
            os.remove("Base.json")

        if os.path.exists("Rectangle.json"):
            os.remove("Rectangle.json")

        if os.path.exists("Square.json"):
            os.remove("Square.json")

        rect_output = Rectangle.load_from_file()
        self.assertEqual(rect_output, [])

        square_output = Square.load_from_file()
        self.assertEqual(square_output, [])

        warn = "Base.load_from_file() takes 1 positional argument but 2 were given"

        with self.assertRaises(TypeError) as msg:
            Rectangle.load_from_file('Monty Python')

        self.assertEqual(warn, str(msg.exception))

    def test_create(self):
        """
        Test the create method
        """
        with self.assertRaises(TypeError) as msg:
            warn = Rectangle.create('Monty Python')

        self.assertEqual(
            "Base.create() takes 1 positional argument but 2 were given",
            str(msg.exception)
        )
