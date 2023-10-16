#!/usr/bin/python3
"""TestRectangle class for test"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """TestRectangle class"""

    def tets(self):
        m = Rectangle(1, 2)
        self.assertEqual(m.id, 1)

        m1 = Rectangle(1, 2, 0, 0, 10)
        self.assertEqual(m1.id, 10)
        self.assertTrue(type(m1), Rectangle)

        with self.assertRaises(TypeError):
            r1 = Rectangle(1, "string")
        with self.assertRaises(TypeError):
            r1 = Rectangle("string", 1)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, "4")

        with self.assertRaises(TypeError):
            r1 = Rectangle()
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, 3, 4, 5, 6)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 1.2, 3, 4, 5)
        with self.assertRaises(TypeError):
            r1 = Rectangle(1, 2, None, 4, 5)
        with self.assertRaises(ValueError):
            r1 = Rectangle(-1, 2, 3, 4)
        with self.assertRaises(ValueError):
            r1 = Rectangle(1, 2, 3, -4)
        a = Rectangle(5, 2)
        self.assertEqual(a.area(), 10)
