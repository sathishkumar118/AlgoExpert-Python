def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    return max(maxSubsetSumNoAdjacent(array[1:]),array[0]+maxSubsetSumNoAdjacent(array[2:]))