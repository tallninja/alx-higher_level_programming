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

    for i in range(1, count + 1):
        print("{:d}: {:s}".format(i, argv[i]))
