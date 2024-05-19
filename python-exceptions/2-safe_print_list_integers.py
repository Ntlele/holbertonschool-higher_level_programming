#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for item in range(x):
        try:
            print("{:d}".format(my_list[item]), end="")
        except IndexError:
            break
        except (ValueError, TypeError):
            continue
        else:
            printed += 1
    print()
    return printed
