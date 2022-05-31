#!/usr/bin/python3
for i in range(26, 0, -1):
    char = chr(97 + (i - 1))
    if i % 2 != 0:
        char = chr(ord(char) - 32)
    print("{:s}".format(char), end="")
