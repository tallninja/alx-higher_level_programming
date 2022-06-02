#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    argc = len(argv) - 1
    argmnt = "argument"

    if argc > 1 or argc == 0:
        argmnt += "s"

    if argc == 0:
        argmnt += "."
    else:
        argmnt += ":"

    print("{:d} {:s}".format(argc, argmnt))

    for i in range(1, argc + 1):
        print("{:d}: {:s}".format(i, argv[i]))
