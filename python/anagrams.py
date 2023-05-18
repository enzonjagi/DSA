#!/usr/bin/python

"""
The purpose of this file is to check if two strings supplied are anagrams.
Anagram is a string formed by rearranging another string.

The idea is to check if all the letters in 'string_a',
are all the strings in 'string_b'.

Steps I'll be using:
    1. Receive 'string_a' and 'string_b' as input.
    2. Check the length of both strings to see if they match, 
    if they don't they are not anagrams, if they do proceed to, 
    3. Loop through each unique letter in 'string_a' twice to check if it occurs 
    the same number of times on both strings.
    4. if one letter does not match in number of occurences,
    then they are not anagrams.
    5. if all letter match in number of occurences, 
    then the strings are anagrams of each other.

TODO Add the complexity analysis of this file here:
"""
import sys, re

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

def compare_occurence(char, string_a, string_b):
    """Using this to compare the occurences of a char in 2 strings
    
    Parameter:
        * char: the character
        * string_a
        * string_b
    Returns:
        * 1 - if the occurrences are equal
        * 0 - if the occurrences are not equal
    """

    char_occurence_a = 0
    char_occurence_b = 0

    char_occurence_a = char_occurence(char, string_a)
    char_occurence_b = char_occurence(char, string_b)

    if char_occurence_a == char_occurence_b:
        are_match = 1
    else:
        are_match = 0
    
    return are_match
    

def are_anagrams(string_a, string_b):
    """The purpose of this file is to check if two strings supplied are anagrams.
    
    Anagram is a string formed by rearranging another string.
    The idea is to check if all the letters in 'string_a',
    are all the strings in 'string_b'.
    
    Parameters:
        * string_a
        * string_b
    returns:
        * "'string_a' and 'string_b' are/are not anagrams" 
    """

    anagram_status = ''
    length, count = 0, 0

    if len(string_a) != len(string_b):
        anagram_status = f'\'{string_a}\' and \'{string_b}\' are not anagrams'
        return anagram_status
    else:
        length = len(string_a)
        while count < length:
            char = string_a[count]
            # for char in string_a:
            # TODO Ensure the code only checks letters not all characters
            if re.match("[^a-zA-Z0-9]", char):
                match = compare_occurence(char, string_a, string_b)
                if match == 0:
                    anagram_status = f'\'{string_a}\' and \'{string_b}\' are not anagrams'
                    return anagram_status
            count += 1

        # if the code get's to this point then it means the strings are anagrams
        anagram_status = f'\'{string_a}\' and \'{string_b}\' are anagrams'
    
    return anagram_status


    
print(are_anagrams('name', 'mane'))
print(are_anagrams("I'm a dot in place.", "A decimal point"))
