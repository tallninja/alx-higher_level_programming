#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    count = len(argv) - 1
    argmnt = "argument"

    if count > 1:
        argmnt += "s"

    if count == 0:
        argmnt += "."
    else:
        argmnt += ":"

    print("{:d} {:s}".format(count, argmnt))

    for i in range(count):
        print("{:d}: {:s}".format((i + 1), argv[i + 1]))
