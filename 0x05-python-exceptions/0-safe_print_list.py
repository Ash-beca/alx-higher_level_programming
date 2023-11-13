#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
     i = 0
    try:
        for ch in range(x):
            print("{}".format(my_list[ch]), end="")
            ch += 1
        print("")
    except IndexError:
        break
    else:
        print("")
    return ch