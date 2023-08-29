#!/usr/bin/python3
def safe_print_list_integers(my_list=[], ch=0):
    ch = 0
    for i in range(ch):
        try:
            print("{:d}".format(my_list[i]), end="")
            ch += 1
        except (ValueError, TypeError):
            continue
    print("")
    return ch