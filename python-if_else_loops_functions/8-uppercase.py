#!/usr/bin/python3
def uppercase(str):
    up_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            up_char = chr(ord(char) - 32)
            up_str += up_char
        else:
            up_str += char
    print("{}".format(up_str))
