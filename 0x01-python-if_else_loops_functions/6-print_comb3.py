#!/usr/bin/python3
"""" print combo of 2 digits  """

for i in range (10):
    for j in range (i, 10):
        print("{}{}".format(i, j), end="")
        print(end=", "if i != 9 or j != 9 else "\n")