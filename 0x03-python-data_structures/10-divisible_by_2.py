#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    newlist = []
    for i in range(len(my_list)):
        newlist.append(my_list[i] % 2 == 0)
    return newlist
