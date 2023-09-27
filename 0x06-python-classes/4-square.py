#!/usr/bin/python3
""" Square class """


class Square:
    """Square"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def area(self):
        if not isinstance(self.__size, int):
            raise Exception('size must be an integer')
        elif self.__size < 0:
            raise Exception('size must be >= 0')

        return self.__size * self.__size
