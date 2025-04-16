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
    if not - inform or request for array

    if array:
        check for empty array - return 0
    else:
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

    tot = 0.0

    if checkInput(arr) == 0:
        # Check inf input is an array
        return ("Please supply a valid array.")

    if len(arr) == 0:
        # check if array is empty
        return 0

    for el in arr:
        if type(el) == int or type(el) == float:
            tot += el

        else:
            return ("The array elements are not integers.")

    return (f"The sum of the array is {tot}")


if len(sys.argv) < 2:
    print("No arguments provided")
else:
    arr = []
    for i in range(1, len(sys.argv)):
        arr.append(i)


    print(sumArray(arr))
