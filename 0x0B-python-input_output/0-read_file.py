#!/usr/bin/python3
"""read_file"""


def read_file(filename=""):
    """read_file"""
    file = open(filename, "r", encoding="utf-8")
    print(file.read())
