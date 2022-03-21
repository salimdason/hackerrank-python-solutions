"""Solution to HackerRank's pyton coding challenge.
@author: Mohammed Salim Dason
@email: salimdason@outlook.com
@twitter: moedason
"""


def plusMinus(arr):
    """
    :param arr: This represents the input array
    :return: We will return the ratio of positive numbers, ratio of negative numbers, and ratio of zeros to
    six decimal places with each printed on a new line.
    """

    # We compute the length of the array. We will need this to calculate the ratios
    len_array = len(arr)

    """
    We will proceed to initialize empty arrays for the positives, negatives and zeros, to which we will append 
    occurrences of each. We count alternatively init a counter and set it to zero and increment it with each occurrence
    by += 1.
    """
    positives = []
    negatives = []
    zeros = []

    """
    Here, we iterate over the array and append each occurrence of positive integers, negative integers, and zeros 
    to their respective arrays as initialized above in the previous step.
    """
    for integer in arr:
        if integer > 0:
            positives.append(integer)
        elif integer < 0:
            negatives.append(integer)
        else:
            zeros.append(integer)

    """
    Now let's compute the ratios for positive integers, negative integers and zeros using the len() method and "/" 
    arithmetic operator. We will then print out the computed ratio to 6 decimal places: 
    
    %.6f -> six decimal places. The number after the ". represents the total number of decimal places.
    """
    positives_ratio = len(positives) / len_array
    print("%.6f" % positives_ratio)

    negatives_ratio = len(negatives) / len_array
    print("%.6f" % negatives_ratio)

    zeros_ratio = len(zeros) / len_array
    print("%.6f" % zeros_ratio)


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
