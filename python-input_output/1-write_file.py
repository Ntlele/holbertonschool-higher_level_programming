#!/usr/bin/python3
"""
This module write a string to a file 
and returns the number of characters writen
"""


def write_file(file_name="", text=""):
    """ This function writes to a file and counts characters """
    with open(file_name, 'w') as file:
        file.write(text)

    return len(text)
