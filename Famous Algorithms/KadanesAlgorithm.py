def kadanesAlgorithm(array):
    currSum = array[0]
    maxSum = currSum
    for item in array:
        currSum += item
        if currSum < 0:
            currSum = 0
        if currSum > maxSum:
            maxSum = currSum
    return maxSum  