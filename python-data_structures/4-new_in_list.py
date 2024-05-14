#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    if idx < 0:
        print("none")
        return my_list
    if idx > len(my_list):
        print("none")
        return my_list
    else:
        new_list = my_list[:]
        new_list[idx] = element
        print("{}".format(new_list))
        print("{}".format(my_list))
        return my_list
