#!/usr/python3

import sys

"""
The purpose of this file is to calculate the number of;
    * Consonants and,
    * Vowels
In a string.

Solution:
    * Calculate the number of consonants
    * Calculate the number of vowels
    * cons_vow_count: Return a string with the sum total of
        consonants and vowels in a string.

TODO: Add the complexity analysis here.
"""


def cons_count(string):

    """Calculate the consonants in a string"""

    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in string:
        if letter.isalpha() and letter not in vowels:
            count += 1

    return count


def vow_count(string):

    """Calculate the number of vowels in a string"""

    vowels = ["a", "e", "i", "o", "u"]
    count = 0

    for letter in string:
        if letter in vowels:
            count += 1

    return count


def cons_vow_count(string):

    """Calculates the consonants and vowels in a string"""

    consonants = 0
    vowels = 0

    if string == '':
        return "Please input a non-empty string"

    consonants = cons_count(string)
    vowels = vow_count(string)

    return f'{string} has {vowels} vowels and {consonants} consonants.'


if len(sys.argv) < 2:
    print("No arguments provided")
else:
    for i in range(1, len(sys.argv)):
        print(cons_vow_count(str(sys.argv[i])))
