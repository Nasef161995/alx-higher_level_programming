#!/usr/bin/python3
""" Square class """


class Square:
    """Square"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise Exception('size must be an integer')
        if value < 0:
            raise Exception('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if type(value) != tuple:
            raise Exception('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.__size:
            s = ''
            for x in range(0, self.__position[0]):
                s += ' '

            for i in range(0, self.__size):
                for j in range(0, self.__size):
                    if j == 0:
                        print(f"{s}#", end='')
                    else:
                        print("#", end='')
                print()
        else:
            print()
