""" Given an array of length N having integers ranging from 1 to N, find the first duplicate values from left to right
"""
def firstDuplicateValue(array):
    # Write your code here.
    cntArray = dict()
    for item in array:
        if item in cntArray:
            return item
        else:
            cntArray.update({item:1})
    return -1
