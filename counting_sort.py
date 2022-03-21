"""Solution to HackerRank's pyton coding challenge.
The counting sort, does not require comparison.
Instead, you create an integer array whose index range covers the entire range of values in your array to sort.
Each time a value occurs in the original array, you increment the counter at that index.
At the end, run through your counting array, printing the value of each non-zero valued index that number of times.


@author: Mohammed Salim Dason
@email: salimdason@outlook.com
@twitter: moedason
"""


def countingSort(arr):
    """ This is pretty straight forward. We first begin by initializing an array wth index range 100
    of zeros, and then for each element in the array we increment its value by 1"""

    zeros = [0] * 100
    for a in arr:
        zeros[a] += 1

    return zeros
