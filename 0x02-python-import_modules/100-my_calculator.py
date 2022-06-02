#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = str(argv[2])
    a = int(argv[1])
    b = int(argv[3])
    result = 0

    if op is '+':
        result = add(a, b)
    elif op is '-':
        result = sub(a, b)
    elif op is '*':
        result = mul(a, b)
    elif op is '/':
        result = div(a, b)
    else:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)

    print("{:d} {:s} {:d} = {}".format(a, op, b, result))
