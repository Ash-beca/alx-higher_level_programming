#!/usr/bin/python3
for x in range(97, 123):  # ASSCI code
    if x != 101 and x != 113:
        print("{:s}".format(chr(x)), end="")