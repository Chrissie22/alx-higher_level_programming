#!/usr/bin/python3
"""Prints the ASCII alphabets in lowercase, except 'q' and 'e'"""

for c in range(97, 123):
    if chr(c) != 'q' and chr(c) != 'e':
        print("{}".format(chr(c)), end="")
