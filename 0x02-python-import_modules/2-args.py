#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    x_arg = len(argv) - 1
    if x_arg == 0:
        print("{}".format("0 arguments."))
    elif x_arg == 1:
        print("{}".format("1 argument:"))
        print("1: {}".format(argv[1]))
    else:
        print("{:d} {}".format(x_arg, "arguments:"))
        for i in range(1, x_arg + 1):
            print("{:d}: {}".format(i, argv[i]))