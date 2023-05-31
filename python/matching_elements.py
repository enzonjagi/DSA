#!/usr/python

import sys
"""
The purpose of this file is to find matching elements in an
integer array.

Solution:
    * match_el: check if two integers match.
    * matching_elements:
        * ensure the element has more than one element,
        * create a nested loop,
        * for each element, loop through the array and,
        * call the previous function to check if they're a match,
        * if there is a match, add the array to a matching_elms array
        * return: the matching_elms array

TODO Add the complexity analysis here.
"""


def match_el(i, j):

    """Checks if two integers match"""

    match = 0

    if int(i) == int(j):
        match = 1

    return match


def arr_add(arr):

    """Adds elements to an array"""

    arr2 = []

    for i in arr:
        arr2.append(i)

    return arr2


def find_matching(arr):

    """Returns two matching elements from an array"""

    matching_elms = []
    arr2 = arr_add(arr)

    if len(arr) < 2:
        return "The array only has one element."
    for el in arr:
        arr2.remove(el)
        for el2 in arr2:
            match = match_el(el, el2)
            if match == 1:
                return f"{el} has a match in the array {arr}."

    return "There are no matching elements in the array."


def matching_elements(arr):

    """Returns an array of matching elements from an array"""

    matching_elms = []
    arr2 = arr_add(arr)

    if len(arr) < 2:
        return "The array only has one element."
    for el in arr:
        arr2.remove(el)
        for el2 in arr2:
            match = match_el(el, el2)
            if match == 1:
                matching_elms.append(el)

    if len(matching_elms) == 0:
        return f"The array {arr} has no matching elements."
    return f"The elements {matching_elms} have a match in the array {arr}."


arry = []
if len(sys.argv) < 2:
    print("Please input a list of integers.")
else:
    for i in range(1, len(sys.argv)):
        check = sys.argv[i]
        if check.isnumeric():
            arry.append(int(sys.argv[i]))

    print(matching_elements(arry))
    print(find_matching(arry))
# print(matching_elements([1, 2, 3, 4, 5, 5, 6, 7, 8, 9, 9, 10]))
# print(matching_elements([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
