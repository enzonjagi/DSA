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
"""
RUBBER DUCK

Problem
- Converting 12 hour AM/PM time into 24 hour Military time.
- 12:00:00 AM -> 00:00:00 (We are substracting 12 from the hour)
- 12:00:00 PM -> 12:00:00 (Remains as is)
- For every other AM hour we'll leave as is.
- For every other PM hour we'll add 12.

Input: time string e.g '12:02:00AM'
OutPut: time string e.g '00:02:00'

NOTE: All inputs are valid.

Solution

- Split the string into 3 parts:
    - the time e.g '12:00:00' (new_time)
    - the time_of_day e.g 'AM' (time_of_day)
- Assign a variable(hour) to the hour part and convert it to integer

- Use the time of day to determine what operation we'll be doing
on the hour variable of the time
    - i.e check for AM or PM
        - check for 12 in the hour part
    - Operations to be made:
        - for PM add 12 but leave as is for 12 PM
        - for AM leave as is, but subtracct 12 from 12 AM
        
- Replace the first two characters of the time (new_time)
with the string version of the (hour) variable.
- Output the new string.

Functions needed:
1. timeConversion(s):
    - split the string and assign variables
    - call the function that does the comparisons
    - do the last operations of the solution
    
2. convertHour(hour, time_of_day):
    - convert hour into integer
    - create a condition to check for AM/PM 
    - and in each condition another for 12(hour)
    - Operations to be made:
        - for PM add 12 but leave as is for 12 PM
        - for AM leave as is, but subtracct 12 from 12 AM
    - convert the hour variable back to a string and return it
"""

def convertHour(hour, time_of_day):
    '''
    Use the time of day to determine what operation we'll be doing
    on the hour variable of the time
    '''
    
    n_hour = int(hour)
    hour = hour
    
    if time_of_day == 'AM' and n_hour == 12:
        n_hour -= 12
        hour = "0" + str(n_hour)
    elif time_of_day == 'PM' and n_hour != 12:
        n_hour += 12
        hour = str(n_hour)

    return hour

        

def timeConversion(s):
    """
    timeConversion(s):
    - split the string and assign variables
    - call the function that does the comparisons
    - do the last operations of the solution
    """
    
    length = len(s)
    new_time = s[0:length-2]
    time_of_day = f"{s[length-2]}{s[length-1]}"
    hour = s[0:2]
    
    n_hour = convertHour(hour, time_of_day)
    

    return f"{n_hour}{new_time[2:length]}"
    
    
print(timeConversion("07:05:45PM"))
print(timeConversion("12:05:45PM"))
print(timeConversion("07:05:45AM"))
print(timeConversion("12:05:45AM"))