#!/usr/bin/python3
"""write_file"""


def write_file(filename="", text=""):
    """write_file"""
    with open(filename, "w", encoding="utf8") as file:
        file.write(text)

    return len(text)
