#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    num = 0
    num_p = 0
    try:
        while num < x:
            value = my_list[num]
            if type(value) == int:
                print("{:d}".format(my_list[num]), end="")
                num_p += 1
            num += 1
    except (ValueError, IndexError):
        pass
    return num
