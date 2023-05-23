#!/usr/bin/python

"""
Hackerrank Question:
Given five positive integers, find the minimum and maximum values 
that can be calculated by summing exactly four of the five integers. 
Then print the respective minimum and maximum values 
as a single line of two space-separated long integers.

Steps to solution below:
    1. find the smallest and largest values in the array
    2. to calculate minSum and maxSum, cater for value where largest == smallest
    3. for minSum, add all values except the largest
    3. for maxSum, add all value except the smallest
    4. if largest and smallest values are equal(meaning the whole array was added to minSum and maxSum), 
    5. then subtract value of the largest from both minSum and maxSum
    6. print out minSum and maxSum

TODO Add the complexity analysis here
"""

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
def check_smallest(arr):
    """checks for smallest value in an array"""

    if len(arr) < 1:
        return 0
    else:
        smallest = arr[0]
        for i in arr:
            if i < smallest:
                smallest = i
    
    return smallest


def check_largest(arr):
    """checks largest value in array"""

    if len(arr) < 1:
        return 0
    else:
        largest = arr[0]
        for i in arr:
            if i > largest:
                largest = i
    
    return largest


def miniMaxSum(arr):
    """Find the maxSum and minSum and print both values"""
    
    largest = check_largest(arr)
    smallest = check_smallest(arr)
    minSum = 0
    maxSum = 0

    if len(arr) < 1:
        print("Array is empty")
        return 0
    else:
        for i in arr:
            if i != largest or smallest == largest:
                minSum += i
        for i in arr:
            if i != smallest or smallest == largest:
                maxSum += i
    
    if largest == smallest:
        minSum -= largest
        maxSum -= largest
        
    # print (f'{minSum} {maxSum}')
    return f"{minSum} {maxSum}"
            
print(miniMaxSum([-4, 3, -9, 0, 4, 1]))
print(miniMaxSum([5, 5, 5, 5, 5]))

