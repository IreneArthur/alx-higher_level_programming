#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    newlist = []
    try:
        for i in range(list_length):
            try:
                result = my_list_1[i] / my_list_2[i]
            except ZeroDivisionError:
                print("division by 0")
                return None
            except ValueError:
                print("wrong type")
                return None
    except IndexError:
        pass
    else:
        newlist.append(result)
    finally:
        return newlist
        