#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
rem = abs(number) % 10
if number < 0:
    rem = -abs(rem)

if rem == 0:
    txt = "and is 0"
elif rem > 5:
    txt = "and is greater than 5"
elif rem < 6:
    txt = "and is less than 6 and not 0"

print(f"Last digit of {number} is {rem} {txt}")
