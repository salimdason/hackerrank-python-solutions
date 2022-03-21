"""Solution to HackerRank's pyton coding challenge.

Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Example: Given this square matrix, the left-to-right diagonal = 1 + 5 + 9 = 15
and the right-to-left diagonal = 3 + 5 + 9. Therefore the absolute difference of the sum of the
square matrix's two diagonals -> |15-17| = 2
    1 2 3
    4 5 6
    9 8 9

@author: Mohammed Salim Dason
@email: salimdason@outlook.com
@twitter: moedason
"""

arr = [[1, 2, 3, 4], [4, 5, 6, 7], [8, 9, 10, 11], [12, 13, 14, 15]]


def diagonalDifference(arr):
    """Obviously the following code can be refactored and improved. However, this
    here is to simplify the process as much as possible. so we begin by initializing two empty
    arrays. The first diagonal and the second diagonal"""
    first_diagonal = []
    second_diagonal = []

    """Now loop through the parent array(square matrix) and then append elements in their 
    respective positions to the first diagonal and do same for the second diagonal.
    Finally sum the first and the second and find their difference, and return the absolute value of
    the differential."""
    for i in range(len(arr)):
        first_diagonal.append(arr[i][i])
        second_diagonal.append(arr[i][-(i + 1)])
        result = sum(first_diagonal) - sum(second_diagonal)
    return abs(result)


if __name__ == "__main__":
    print(diagonalDifference(arr))


