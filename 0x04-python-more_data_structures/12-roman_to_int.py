#!/usr/bin/python3

def roman_to_int(roman_string):
    if roman_string:
        roman_numbers = {
            'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000
        }
        return (sum([roman_numbers.get(char) for char in roman_string]))
    return (0)
