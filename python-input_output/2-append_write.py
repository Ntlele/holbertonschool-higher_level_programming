#!/usr/bin/python3
"""
This module appends content to the end of the file
and returns the number of charactors added
"""


def append_write(filename="", text=""):
    """ This function appends content to the end of the file """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
