#!/usr/bin/python3
"""Print the alphabet in lowercase, not followed by a new line."""

for letter in range(97, 123):
    if letter != 101 & letter != 113:
        print("{}".format(chr(letter)), end="")