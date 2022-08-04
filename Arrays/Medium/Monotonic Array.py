"""
A method which takes in an array and checks whether it is non-increasing or non-decreasing
"""
def isMonotonic(array):
    boolIncreasing = None
    for i in range(len(array)-1):
        if array[i] == array[i + 1]:
            continue
        elif boolIncreasing == None:
                boolIncreasing = array[i] < array[i + 1]
        elif boolIncreasing ^ (array[i] <= array[i + 1]):
                return False
    return True
    pass
