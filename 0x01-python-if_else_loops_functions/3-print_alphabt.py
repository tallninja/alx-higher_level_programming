#!/usr/bin/python3
for i in range(26):
    if chr(97 + i) != 'e' and chr(97 + i) != 'q':
        print("{:s}".format(chr(97 + i)), end="")
