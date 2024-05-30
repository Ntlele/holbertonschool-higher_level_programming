#!/usr/bin/python3
"""
This module that returns an object represented by the JSON string
"""


def from_json_string(my_string):
    """ Returns the object represented by a JSON string """


    if isinstance(my_string, str):
        try:
            return eval(my_string)
        except SyntaxError:
            return None
    else:
        return None
