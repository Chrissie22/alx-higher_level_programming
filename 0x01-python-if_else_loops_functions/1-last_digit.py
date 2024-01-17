#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
digit = abs(number) % 10
if (number < 0):
    digit = -digit
print(f"Last digit of {number:d} is {digit:d} and ", end="")
if digit > 5:
    print(f"is greater than 5")
elif digit == 0:
    print(f"is 0")
elif digit < 6 and digit != 0:
    print(f"is less than 6 and not 0")
