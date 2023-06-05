#!/usr/bin/python3

"""
The purpose of this file is to reverse an array.

Steps:
    1. Receive an array and initiate an empty array, plus a counter
    2. If the length is less than one, return the same array
    3. with counter being equal to length - 1 and greater & equal to 0
    4. add the arr[counter] to the empty array, decrementing counter each time.

Alternative:
    1. Equate the value of empty array to the reverse i.e arr[-1:0]

TODO: Add complexity analysis here.
"""
import sys


def reverse_arr(arr):

    """Reverses an array"""

    reverse = []
    length = len(arr)
    counter = length - 1

    if length < 2:
        return arr

    while counter >= 0:
        reverse.append(arr[counter])
        counter -= 1

    return reverse


arr = []
if len(sys.argv) < 2:
    print("please input an array in list form, with items separated in spaces")
else:
    for i in range(1, len(sys.argv)):
        arr.append(str(sys.argv[i]))
    print(f"The array {arr} is reversed to: {reverse_arr(arr)}")
