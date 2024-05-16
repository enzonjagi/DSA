#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
"""
RUBBER DUCK

Problem

- Goal: to determine the number of times Maria breaks her records,
    for most and least points.
- Input: scores per game - a list of scores
    * The first line contains an integer , the number of games.
    * The second line contains  space-separated integers describing
    the respective values of
    * the code already split this and made a list of elements from it
- Return: an array with 2 elements:
    * index 0: breaking most points(maximum) record
    * index 1: breaking least points(minimum) record
    
Solution

- scores as our input
- assign the first score to max_val and min_val
- initialize two values(max_change, min_change) to 0
- loop through the scores
    - each time a score is larger than max_val
    we increment max_change and change max_val to the score
    - each time a score is smaller than min_val 
    we increment min_change and change min_val to the score
- at the end we return an array with max_change and min_change

"""


def breakingRecords(scores):
    # Write your code here
    max_score = scores[0]
    min_score = scores[0]
    length = len(scores)
    new_scores = scores[1:length]
    changes = [0, 0]

    for score in new_scores:
        if score > max_score:
            max_score = score
            changes[0] += 1
        if score < min_score:
            min_score = score
            changes[1] += 1

    return changes


print("Please input the length of the array:")
n = int(input().strip())
print("Please input the array elements separated by spaces:")

scores = list(map(int, input().rstrip().split()))

result = breakingRecords(scores)

print(result)
