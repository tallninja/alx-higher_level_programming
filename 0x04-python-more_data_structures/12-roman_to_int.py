#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or type(roman_string) is not str:
        return 0
    roman_d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    i = 0
    number = 0
    for i in range(len(roman_string) - 1, -1, -1):
        num = roman_d[roman_string[i]]
        if 3*num < number:
            number -= num
        else:
            number += num
    return number
