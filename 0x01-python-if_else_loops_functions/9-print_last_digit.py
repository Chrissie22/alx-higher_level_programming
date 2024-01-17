#!/usr/bin/python3
# Author - Christabel Ojobolo

def print_last_digit(number):
    """Prints and return the last digit of number"""
    print(abs(number) % 10), end="")
    return (abs(number) % 10)
