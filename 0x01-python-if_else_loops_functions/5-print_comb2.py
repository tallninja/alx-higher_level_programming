#!/usr/bin/python3
for i in range(100):
    if i == 99:
        print("{:d}".format(i))
    else:
        print("{}{:d}".format("0" if i < 10 else "", i), end=", ")
