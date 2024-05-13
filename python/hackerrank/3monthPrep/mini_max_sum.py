#!/bin/python3

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
"""
Goal: Minimum sum and maximum sum

Functions:
    1. minSum(arr): calculates the minimum sum
    2. maxSum(arr): calculates the maximum sum
    3. miniMaxSum(arr): output the minimum and maximum 
    sums of the items in the array.
"""
def sumArr(arr):
    # returns a sorted arr
    sumArr = 0
    
    for a in arr:
        sumArr += a
        
    return sumArr
    
def minSum(arr):
    # returns the sum of the first four items.
    length = len(arr)
    minArr = arr[0:length-1]
    
    minSum = sumArr(minArr)
    
    return minSum
    
def maxSum(arr):
    # returns the sum of the first four items.
    length = len(arr)
    maxArr = arr[1:length]
    
    maxSum = sumArr(maxArr)
    
    return maxSum
    

def miniMaxSum(arr):
    # Write your code here
    length = len(arr)
    
    if length < 5:
        if length <= 0:
            return 0
        return sum(arr[0:length-1])
         
    miniSum = minSum(arr)
    maxiSum = maxSum(arr)
    
    print(f"{miniSum} {maxiSum}")

print(miniMaxSum([1,4,5,2,6]))
print(miniMaxSum([9,4,3,2,6]))
print(miniMaxSum([1,2,3,9,6]))