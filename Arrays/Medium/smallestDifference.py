"""
A Method which takes in two non-empty arrays of integers and finds a pair(one from each array) which has the least absolute difference.
"""
def smallestDifference(arrayOne, arrayTwo):
    # Write your code here.
    arrayOne.sort()
    arrayTwo.sort()
    absDiff = float("inf")
    res = []
    i,j = 0,0
    while absDiff > 0 and i < len(arrayOne) and j < len(arrayTwo):
        if absDiff > abs(arrayOne[i] - arrayTwo[j]):
            absDiff = abs(arrayOne[i] - arrayTwo[j])
            res = [arrayOne[i], arrayTwo[j]]
        if arrayOne[i] > arrayTwo[j]:
            j += 1 
        else:
            i += 1
    return res
    pass
