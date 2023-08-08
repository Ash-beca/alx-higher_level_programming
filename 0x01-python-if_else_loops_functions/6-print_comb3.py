#!/usr/bin/python3
for x in range(9):
    for i in range(x + 1, 10):
        if x * 10 + i < 89:
            print("{:d}{:d}".format(x, i), end=", ")
print("{:d}".format(89))