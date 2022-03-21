"""Solution to HackerRank's pyton coding challenge.

Given an array of integers, where all elements but one occur twice, find the unique element.
Example: array = [ 1, 2, 1, 1, 2, 6, 8, 8, 6, 7]
The function should return 7 since it is the only element that apppears once.



@author: Mohammed Salim Dason
@email: salimdason@outlook.com
@twitter: moedason
"""
arr = [3, 3, 4, 5, 4, 5, 0, 0, 8, 6, 6, 8]


def lonelyInteger(arr):
    """This simply requires looping through each element of the array and counting its occurance.
    if it appears more than once, we do nothing, else we return it."""

    for i in arr:
        if arr.count(i) > 1:
            pass  # Do absolutely nothing
        else:
            return i



