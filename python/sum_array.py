#!/bin/python3

import math
import os
import random
import re
import sys

"""
## 20. How do you sum all the elements in an array?

Problem:
    Find the sum of elements in an array

To Think about
    Check for an array - input should be an array
    if not - inform or request for elements of an array

    TODO: check if array elements are integers?

    we could call the sum function with the array

    or

    we could have a total variable of value 0,
    then loop through array adding each element to total


"""

def checkInput(el):
    """
    Checks if the input supplied is an array.

    el should be the input
    """
    out = 0

    if isinstance(el, list):
        out = 1
    
    return out

def sumArray(arr):
    """
    Returns the sum of elements in an array
    """

    tot = 0


    for el in arr:
        tot += el
    
    tot = round(tot, 4)
    return (tot)
    #return sum(arr)


arr = []
if len(sys.argv) < 2:
    # In case of empty array i.e no elements given, write this
    print("please input an array in list form, with items separated in spaces")
else:
    
    try:
        for i in range(1, len(sys.argv)):
            arr.append(float(sys.argv[i]))
        print(f"{sumArray(arr)}")

    except ValueError:
        # In the case where elements are not numbers
        print("please input numbers in list form, separated with spaces")
