#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle

my_square = Rectangle.suare(5)
print("Area: {} - perimeter: {}".format(my_square.area(), my_square.perimeter()))
print(my_square)
