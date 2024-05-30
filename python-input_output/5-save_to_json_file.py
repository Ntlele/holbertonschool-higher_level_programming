#!/usr/bin/python3
"""
This module writes an object to a text file
using a JSON representation
"""

def save_to_json_file(my_obj, filename):
    """ Writes an object to a text file using JSON representation """
    with open(filename, 'w') as file:
        file.write(to_json_string(my_obj))

def to_json_string(my_obj):
    """ Returns an object as JSON """
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
