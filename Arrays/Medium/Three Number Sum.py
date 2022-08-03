"""
Problem Statement:
A method that takes in a non-empty array which identifies triplets in the array summing up to the targetSum with each of them arranged in ascending order
"""
def twoNumberSum(array,targetSum,currNum):
    res = []
    for i in range(len(array)):
        if array[i] < targetSum:
            try:
                array[i+1:].index(targetSum-array[i])
                res.append([currNum,array[i],targetSum - array[i]])
            except:
                continue
        else:
            break
    return res
def threeNumberSum(array, targetSum):
    array.sort()
    res = []
    for i in range(len(array)):
        if array[i] < targetSum:
            res += twoNumberSum(array[i+1:],targetSum - array[i],array[i])
        else:
            break
    return res
        
