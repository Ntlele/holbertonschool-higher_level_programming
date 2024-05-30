#!/usr/bin/python3
""" This module opens and reads the file content """


def read_file(filename=""):
    """ This function reads the file content """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
