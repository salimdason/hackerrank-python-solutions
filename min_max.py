"""Solution to HackerRank's pyton coding challenge.
Given five positive integers, find the minimum and maximum values that
can be calculated by summing exactly four of the five integers. Then print
the respective minimum and maximum values as a single line of two space-separated
long integers.

Example: array = [1, 3, 5, 7, 9]

The minimum sum is 1 + 3 + 5 + 7 = 16
The maximum sum is 3 + 5 + 7 + 9 = 24

@author: Mohammed Salim Dason
@email: salimdason@outlook.com
@twitter: moedason
"""
arr = [10, 13, 15, 17, 20]


def miniMaxSum(arr):
    """
    The function takes an input array of length = 5 as a parameter, and return the minimum and maximum
    values that can be calculated by summing exactly four of the five integers.
    """
    """
    Let's first begin by sorting the array, proceeding without doing so will make our work complicated.
    So we call the sort method on the input array. i.e array.sort()
    """
    arr.sort()

    """
    Since we are given the length of the array before hand, we can then simply proceed to sum the
    first 4 elements of the array by calling the sum() method on the indexed array. [0:4]
    i.e From the first element to the 4th element (index 3). The number that comes after ":" is not inclusive.
    
    We do the same thing for the maximum sum. This time, we start from the second element (index 1) 
    all the way to the end of the list (index 5). Then we simply print the output. Voila!
    """
    min_sum = sum(arr[0:4])
    max_sum = sum(arr[1:])

    print('{} {}'.format(min_sum, max_sum))


if __name__ == '__main__':
    miniMaxSum(arr)
