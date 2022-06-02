#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    from calculator_1 import add, sub, mul, div

    argc = len(argv) - 1

    if argc != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    op = str(argv[2])
    ops = "+-*/"

    if op not in ops:
        print("Unknown operator. Available operators: +, -, * and / ")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    result = 0

    if op == "+":
        result = add(a, b)
    elif op == "-":
        result = sub(a, b)
    elif op == "*":
        result = mul(a, b)
    elif op == "/":
        result = div(a, b)
    print("{:d} {:s} {:d} = {}".format(a, op, b, result))
