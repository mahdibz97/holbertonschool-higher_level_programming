#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    len = 0
    try:
        for i in range(0, x):
            print("{}".format(my_list[i]), end="")
            len += 1
        print()
    except IndexError:
        print()
        return len
    return len
