#!/usr/bin/python3
import sys

if __name__ == "__main__":
    add_arg = 0
    for i in sys.argv[1:]:
        sum_arg += int(i)
    print("{:d}".format(add_arg))