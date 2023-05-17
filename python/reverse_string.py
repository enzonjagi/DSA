#!/usr/bin/python
"""
The code in here reverses a value(string, int, float),
by using the following steps:
    1. Receive value from user
    2. Store number in a temporary variable
    3. Reverse the value

PS: Complexity analysis not done yet
"""

import sys

n = len(sys.argv)

def reverse_value(val):
    """Code to reverse the value
    
    parameters: 
        - value to be reversed
    return: 
        - Reversed value
    """

    temp = str(val)
    counter = len(temp) - 1
    reversed = ''

    while counter >= 0:
        reversed += temp[counter]
        counter -= 1
    
    return reversed

for i in range(1, n):
    num = sys.argv[i]
    reverse =  reverse_value(num)
    print(f'Value: {sys.argv[i]} --> Reversed as: {reverse}')