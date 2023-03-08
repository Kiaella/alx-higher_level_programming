#!/usr/bin/python
# Author - Odoemenam El

def uppercase(str):
    """print a string in uppercase."""
    for c in str:
        if ord(c) >= 97 and ord(c) <= 122:
            c = chr(ord(c) - 32)
            print("{}".format(c), end="")
            print("")
