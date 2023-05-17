#!/usr/bin/python
"""
The code in here checks to see if a given value is a palindrome,
by using the following steps:
    1. Receive value from user
    2. Store value in a temporary variable
    3. Reverse the value
    4. compare the value stored in the temp var to the reversed value
    5. if they are equal, then the value is a palindrome
    6. if they are not equal then it is not.

PS: Complexity analysis not done yet
"""

import sys

n = len(sys.argv)

def reverse_value(val):
    """Code to reverse a value
    
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

def check_palindrome(val):
    """Code to check if a value is a palindrome
    
    parameters: 
        - the value to be checked
    return: 
        - Palindrome or Not Palindrome
    """

    temp = val
    reversed = reverse_value(val)

    # check if the numbers are equal
    if temp == reversed:
        return "Palindrome"
    return "Not Palindrome"

if len(sys.argv) > 1:
    for i in range(1, n):
        num = sys.argv[i]
        pal_status =  check_palindrome(num)
        print(f'Value: {sys.argv[i]} --> {pal_status}')
else:
    print("Please supply Input after the filename.")