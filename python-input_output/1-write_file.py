#!/usr/bin/python3
"""
This module write a string to a file 
and returns the number of characters writen
"""


def write_file(file_name="", text=""):
    """ This function writes to a file and counts characters """
    # Open the file in write mode and write the text to it
    with open(file_name, 'w') as file:
        file.write(text)
    
    # Return the number of characters written
    return len(text)