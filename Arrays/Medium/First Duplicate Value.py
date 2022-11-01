""" Given an array of length N having integers ranging from 1 to N, find the first duplicate values from left to right
"""
def firstDuplicateValue(array):
    # Write your code here.
    for i in range(len(array)):
        if array[abs(array[i]) - 1] < 0:
            return abs(array[i])
        else:
            array[abs(array[i]) - 1] *= -1
    return -1
