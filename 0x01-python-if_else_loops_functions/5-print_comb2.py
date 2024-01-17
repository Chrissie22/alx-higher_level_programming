#!/usr/bin/python3
"""Prints numbers from 0 to 99"""

for i in range(10):
    for j in range(9):
        if i == 9 and j == 8:
            print("{}{}".format(i, j))
        else:
            print("{}{}, ".format(i, j), end="")
