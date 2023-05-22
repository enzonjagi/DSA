#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
# 
# Thought process
"""
Thought process:
    1. Check the last two indexes of the string for either AM or PM
    2. if PM then we add 12 the hour segment(first part of the string)
    3. if AM then we leave the hour as is
    4. remove the AM or PM parts of the string and return the remainder

"""
def check_time(s):
    # checks for AM or PM
    # returns 0 for AM and 1 for PM
    length = len(s)
    new_str = f'%s%s' % (s[length-2], s[length-1])
    first = f'%s%s' %(s[0], s[1])
    
    if new_str == "AM":
        if first == "12":
            return -12
        else:
            return 0
    elif new_str == "PM":
        if first == "12":
            return 12
        else:
            return 1

def timeConversion(s):
    # Write your code here
    
    # check for AM or PM
    time_check = check_time(s)
    if s == "":
        return f'%s is empty' %(s)
    elif time_check == 0 or time_check == 12:
        # To leave hour as is and remove the AM part
        new_time = f'%s' % (s[0:-2])
        return new_time
    elif time_check == 1:
        # To add 12 to the hour count and remove the PM part
        hour = f'%s%s' % (s[0], s[1])
        hour = int(hour)
        hour = 12 + hour
        new_time = f'%d%s' % (hour, s[2:-2])
        return new_time
    elif time_check == -12:
        # To add 12 to the hour count and remove the PM part
        hour = f'%s%s' % (s[0], s[1])
        hour = int(hour)
        hour = hour - 12
        new_time = f'0%d%s' % (hour, s[2:-2])
        return new_time

print("07:05:45AM in military time is " + timeConversion("07:05:45AM"))
print("07:05:45PM in military time is " + timeConversion("07:05:45PM"))
print("12:05:45AM in military time is " + timeConversion("12:05:45AM"))
print("12:05:45PM in military time is " + timeConversion("12:05:45PM"))