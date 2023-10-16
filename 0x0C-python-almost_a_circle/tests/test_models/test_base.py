#!/usr/bin/python3
"""TestBase class for test"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestBase class"""

    def tets(self):
        m1 = Base()
        self.assertEqual(m1.id, 1)

        m2 = Base()
        self.assertEqual(m2.id, 2)

        m3 = Base(10)
        self.assertEqual(m2.id, 10)
