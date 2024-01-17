#!/usr/bin/python3
"""Prints the ASCII alphabets, in lowercase, not followed by a new line"""

for c in range(97, 123):
    print("{}".format(chr(c)), end="")
