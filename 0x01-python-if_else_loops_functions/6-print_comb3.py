#!/usr/bin/python3
for x in range(9):
    for i in range(x + 1, 10):
        if x < 8:
            print("{:d}{:d}".format(x, i), end=", ")
        else:
            print("{:d}".format(x, i))