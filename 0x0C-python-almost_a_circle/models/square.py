#!/usr/bin/python3
"""Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}"

    def update(self, *args, **kwargs):
        if args:
            attr_names = ['id', 'size', 'x', 'y']
            for i, j in zip(attr_names, args):
                setattr(self, i, j)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        d = {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }
        return d
