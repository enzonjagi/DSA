#!/usr/bin/python

"""
The purpose of this file is to find the number of occurences of a character in
a string:
    1. Receive the characters and strings we're to compare.
    2. Check if both input are valid.
    3. Convert both inputs to lowercase.
    4. Loop through the string and compare each character to the input character.
    5. Each time there's a match increment a counter.
    6. Once we're done looping through, return the value of the counter.

TODO Add the complexity analysis notes here
"""

import sys

def char_occurence(char, string):
    """Find the number of occurences of a character in a string
    
    Parameters:
        * char: the character to check for
        * string: the string we're to check for the character
    Return:
        * char_count: the number of times the character appeared in the string
    """

    char_count = 0
    string = string.lower()
    char = char.lower()

    for s in string:
        if char == s:
            char_count += 1

    return char_count

if len(sys.argv) == 3:
    if len(sys.argv[1]) == 1:
        char = sys.argv[1]
        string = sys.argv[2]
        count = char_occurence(char, string)
        print(f'The char \'{char}\' appeared {count} time(s) in the string \'{string}\'.')
    else:
        print("First input is not a single \'character\'")
else:
    print("Please supply a \'character\' and a \'string\' separated by a space after the filename.")