#!/usr/bin/python3
"""" print numbers between 0 and 98 in hexadecimal"""

for numbers in range(99):
    hexa = hex(numbers)
    print("{} = {}".format(numbers, hexa))