#!/usr/bin/python

"""
The purpose of this file is to raise a number to a power



Steps I'll be using:
    1. Check if the power is negative or positive.
    2. Create a counter
    3. if the power is positive, then we count upwards, 
    multiplying the result by the number till counter == power
    4. if the power is negative then we do a negative power
    calculation(TODO)

TODO Add the complexity analysis of this file here:
"""
import sys


def isPositive(num):

    """Checks if a number is positive or negative"""


    state = 0
    if num > 0:
        state = 1
    elif num == 0:
        return 'zero'
    else:
        state = 0

    return state


def power(num, pow):

    """Raises a number to a power"""


    result = 1
    count = 0

    if isPositive(pow) == 1:
        while count < pow:
            result = result * num
            count += 1
    elif isPositive(pow) == 0:
        # raise to a negative power
        pass
    else:
        result = 0

    return result


print(power(2, 2))
print(power(2, 3))
print(power(2, 12))
print(power(-2, 10))
