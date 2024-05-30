#!/usr/bin/python3
"""
This module returns the JSON represantation of an object
"""


def to_json_string(my_obj):
    """ Returns an object to as JSON """


    if isinstance(my_obj, str):
        return f'"{my_obj}"'
    elif isinstance(my_obj, (int, float)):
        return str(my_obj)
    elif isinstance(my_obj, list):
        elements = ', '.join([to_json_string(elem) for elem in my_obj])
        return f'[{elements}]'
    elif isinstance(my_obj, dict):
        pairs = ', '.join([f'"{key}": {to_json_string(value)}' for key, value in my_obj.items()])
        return f'{{{pairs}}}'
    else:
        return None
