#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if x != y and x < y:
            if (str(x) + str(y)) != "89":
                print("{}{}".format(x, y), end=", ")
print("89")
