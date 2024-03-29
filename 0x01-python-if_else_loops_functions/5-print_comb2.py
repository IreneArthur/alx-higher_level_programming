#!/usr/bin/python3
"""" print numbers from 0 to 99 """

for numbers in range(100):
    print("{:2d}".format(numbers), end="")
    print(end=", "if numbers != 99 else "\n")