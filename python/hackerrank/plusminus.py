#!/usr/bin/python

"""
The Purpose of this file is to 
find the ratio of zeros, positive, and negative numbers
in an array.
Steps:
    1. Check if the arr is empty, if so print that
    2. if not loop through the array
    3. count the negative, positive, and zeros
    4. add count for each
    5. once we're done looping
    6. we calculate the ratios
    7. then print the ratios in 6 decimal places

TODO add complexity analysis here.
"""


def plusMinus(arr):
    # Write your code here
    
    full = len(arr)
    neg = 0
    pos = 0
    zeros = 0
    
    # check if the arr is empty
    if full < 1:
        return "The array is empty"
    else:
        # loop through the array
        # count the negative, positive, and zeros
        # add count for each
        for a in arr:
            if a == 0:
                zeros += 1
            elif a < 0:
                neg += 1
            else:
                pos += 1
                
        # Determine the ratios
        ratio_neg = neg / full
        ratio_pos = pos / full
        ratio_zeros = zeros / full
    
    print ("%.6f\n%.6f\n%.6f\n" % (ratio_pos, ratio_neg, ratio_zeros))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

plusMinus(arr)
plusMinus([6])
plusMinus([-4, 3, -9, 0, 4, 1])