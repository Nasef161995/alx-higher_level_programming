#!/usr/bin/python3
"""Base"""
import json


class Base:
    """Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        self.id = id
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        json_string = json.dumps(list_dictionaries)
        if list_dictionaries is None:
            return "[]"
        else:
            return json_string

    @classmethod
    def save_to_file(cls, list_objs):
        filname = f"{cls.__name__}.json"
        with open(filname, "w", encoding='utf-8') as file:
            json.dump(list_objs, file)
