#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#
"""
Input: An array of integers
The goal: to Calculate the ratios of positive, negative, 
    and zeros in the array.
    
Functions needed:
    1. plusMinus(arr):
        prints: proportion of positive, negative, and zeros
        in that order.
    2. checkNumber(n): checks for positve negative and zero
    3. calcRatio(objectCount, totalObjects):
        Outputs the fraction of a value in 6 decimal values
"""
def checkNumber(n):
    # checks for positve negative and zero
    if n < 0:
        status = -1
    elif n > 0:
        status = 1
    else:
        status = 0
    
    return status
        
    
def calcRatio(objectCount, totalObjects):
    # Outputs the fraction of a value in 6 decimal values
    if objectCount <= 0:
        return 0
    ratio = objectCount/totalObjects
    
    return ("%.6f" % ratio)
    


def plusMinus(arr):
    # Write your code here
    positives = 0
    negatives = 0
    zeros = 0
    total = len(arr)
    
    if total < 1:
        print("Empty Array")
    
    for a in arr:
        if checkNumber(a) == 1:
            positives += 1
        elif checkNumber(a) == -1:
            negatives += 1
        elif checkNumber(a) == 0:
            zeros += 1
            
    # ratio
    print(calcRatio(positives, total))
    print(calcRatio(negatives, total))
    print(calcRatio(zeros, total))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
