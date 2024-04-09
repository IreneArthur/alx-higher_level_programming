#!/usr/bin/python3
def uniq_add(my_list=[]):
    seen = set()
    return sum(filter(lambda x: x not in seen and not seen.add(x), my_list))
