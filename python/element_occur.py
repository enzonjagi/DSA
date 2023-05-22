#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
"""
Given an array of integers, where all elements but one occur twice, 
find the unique element.
Steps to solve this:
    1. Find out how many times the element occurs in the array: 
    we use the first function for this.
    2. Loop through the array checking the element occurence for each
    3. within the loop check if item only occurs once.
    4. if it does return it.
    5. if not continue the loop.

TODO Add complexity analysis below.

"""


def element_occurrence(element, arr):
    # check the number of occurences of an element
    e_occur = 0
    
    for el in arr:
        if el == element:
            e_occur += 1
            
    return e_occur

def lonelyinteger(a):
    # Given an array of integers, where all elements but one occur twice, 
    # this function finds the unique element.
    
    occur_once = 0
    
    if len(a) < 1:
        return "Empty array"
    for el in a:
        el_occur = element_occurrence(el, a)
        if el_occur == 1:
            return el
        
    return "No element occurs once"

def lonely_integers(a):
    # Given an array of integers, where all elements but one occur twice, 
    # this function finds the unique elements in the array.
    # returns an array of elements that occur once.
    
    occur_once = []
    
    if len(a) < 1:
        return "Empty array"
    for el in a:
        el_occur = element_occurrence(el, a)
        if el_occur == 1:
            occur_once.append(el)
        
    return occur_once

print(lonelyinteger([1,1,2,2,3,4,4,5,6,6]))
print(lonelyinteger([1,1,2,2,3,4,4,5]))
print(lonely_integers([1,1,2,2,3,4,4,5]))