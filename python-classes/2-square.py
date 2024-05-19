#!/usr/bin/python3
#-*- coding UTF-8 -*-

"""
2-square.py: contains a class Square that defines a square
"""


class Square:
    """
    class Square represents a square

    Attributes:
        attr1(_Square__size): size of the side of the square (Private)
    """

    def __init__(self, size=0):
        """Initializer with default size = 0"""
        if type(size) is not int:
            raise TypeError("Size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = size
