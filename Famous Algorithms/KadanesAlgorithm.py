def kadanesAlgorithm(array):
    currSum = array[0]
    maxSum = currSum
    for item in array[1:]:
        currSum = max(currSum + item,item)
        if currSum > maxSum:
            maxSum = currSum
    return maxSum