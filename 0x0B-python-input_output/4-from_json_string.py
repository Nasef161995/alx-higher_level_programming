#!/usr/bin/python3
"""from_json_string"""


def from_json_string(my_str):
    """from_json_string"""
    import json
    data = json.loads(my_str)
    return data
