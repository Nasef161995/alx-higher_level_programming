#!/usr/bin/python3
"""to_json_string"""


def to_json_string(my_obj):
    """to_json_string"""
    import json
    new_json = json.dumps(my_obj)
    return new_json
