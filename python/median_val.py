#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def findMedian(arr):
    # Write your code here
    # sort the array
    new_arr = sorted(arr)
    
    # check the length of the array
    length = len(arr)
    
    # use length to find the median
    if length == 0:
        return "Empty array"
    if length % 2 == 0:
        mid = length/2
    else:
        mid = length/2 - 0.5
    mid = int(mid)
    
    median = new_arr[mid]
    
    return median

print(findMedian([1,0,2,3,4,5,6]))
print(findMedian([23,1,45,70,2,3,4,5,6]))