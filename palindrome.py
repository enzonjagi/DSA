#!/usr/bin/python
"""
The code in here checks to see if a number is a palindrome,
by using the following steps:
    1. Receive number from user
    2. Store number in a temporary variable
    3. Reverse the number
    4. compare the number stored in the temp var to the reversed number
    5. if they are equal, then the number is a palindrome
    6. if they are not equal then it is not.
"""

import sys

n = len(sys.argv)

def reverse_number(num):
    """Code to reverse the number - the concept can also be used with a string
    
    parameters: 
        - number to be reversed
    return: 
        - Reversed number
    """
    
    temp = str(num)
    counter = len(temp) - 1
    reversed = ''

    while counter >= 0:
        reversed += temp[counter]
        counter -= 1
    
    return int(reversed)

def check_palindrome(number):
    """Code to check if a number is a palindrome
    
    parameters: 
        - the number to be checked
    return: 
        - Palindrome or Not Palindrome
    """

    temp = number
    reversed = reverse_number(number)

    # check if the numbers are equal
    if temp == reversed:
        return "Palindrome"
    return "Not Palindrome"

for i in range(1, n):
    num = int(sys.argv[i])
    pal_status =  check_palindrome(num)
    print(f'Number: {sys.argv[i]} --> {pal_status}')