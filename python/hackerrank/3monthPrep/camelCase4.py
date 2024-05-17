#!/bin/python3

import math
import os
import random
import re
import sys


# Enter your code here. Read input from STDIN. Print output to STDOUT
"""
RUBBER DUCK

Problem
We are to do one of two things:
    * Split camelCase string into two lowercase strings
    * Combine two lowercase strings into camelCase
There are conditions:
    * Splitting: 
    You'll just get camelCase String and split it. This can be:
        - method name which will have empty parenthesis at the end:
            e.g "camelCase()"
        - class name and variable name:
            just camelCase, no added elements.
            PS: ClassName has all strings starting with capital letters.
    * Combining:
        - method: you create camelCase and add empty parenthesis
            e.g "camel case to camelCase()"
        - variable: create "camelCase" string
            e.g "camel case to camelCase"
        - class: both lowercased strings should have capitalized first
        letter in the CamelCase string. 
            e.g "camel case to CamelCase"

We have input received from STDIN and we return output through STDOUT


Solution
- TODO later: handle all other possible input testcases
 
We get input from STDIN and split it to create an array of 3 elements
for each line of input.

Our function should receive an array with 3 elements:
    * OP: operation 
        - should be "S" or "C" 
        - else "invalid operation - please use "S" or "C"
    * StTyp: type of string to operate on, could be:
        - M: for method
        - C: for class
        - V: for variable
    * InStr: Input string to be operated on, 
    different for each "StTyp":
        - for method : e.g "camelCase()"
        - for variable: e.g "camelCase"
        - for class: e.g "CamelCaseStr"

elements = [Op, StTyp, InStr]
 
camelCase(elements)
        
- Check the Op type to determine function call:    
    * for "S": check for StTyp:
        [Function call]: "split(InStr)"
        - check if there are parenthesis at the end
            * if so, remove them and form a new string
        - we'll have to look for number of capitalized letters
        in the string
        - split string to lowercase strings and add each to
        an array as follows:
            1. from start to letter before capital letter 1
            2. from capital letter 1 to capital letter 2 or end of string
            3. ... continues to last capital letter
            4. from the last capital letter to end of string

        - return array with the lowercase strings
        
        - in the camelCase(elements) function
        return this array as a string:
            * new_array = array[1:length]
            * newString = array[0]
            * for a in new_array:
                newString = newString + " " + a
                
        - return the newString

    * for "C":
        - check for StTyp:
        "combine(StTyp, InStr)"
        - check for whitespace in "InStr"
            - capitalize letters after each whitespace
            - remove whitespaces
        - if StTyp == "M":
            * newString = newString + "()"
        - elif StTyp == "V":
            * newString = newString
        - elif StTyp == "C":
            * capitalize the first character of the String
        - else:
            * inform user that the input is invalid
            
        - return newString
        
        - return newString as is in camelCase(elements) function.

"""