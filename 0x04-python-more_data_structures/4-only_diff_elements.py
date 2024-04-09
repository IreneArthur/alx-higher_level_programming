#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    return list(filter(lambda x: (x in set_1 and x not in set_2)
                       or (x in set_2 and x not in set_1), set_1 | set_2))
