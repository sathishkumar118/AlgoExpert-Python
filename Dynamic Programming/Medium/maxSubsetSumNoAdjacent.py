def maxSubsetSumNoAdjacent(array):
    if len(array) == 0:
        return 0
    curr = array[0]
    return max(maxSubsetSumNoAdjacent(array[1:]),curr+maxSubsetSumNoAdjacent(array[2:]))