"""
Given a Binary tree, find the path with maximum sum. A path cannot have a node with more than 2 connections with other nodes
"""
def maxPathSum(tree):
    return max(newMaxPath(tree))
def newMaxPath(tree):
    if tree == None:
        return [None,None]
    leftPathSum, leftMax = newMaxPath(tree.left)
    rightPathSum, rightMax = newMaxPath(tree.right)
    maxPathSum = int
    if leftPathSum == None and rightPathSum == None:
        return [tree.value,tree.value]
    elif leftPathSum == None:
        maxPathSum = rightPathSum
        leftPathSum = 0
        leftMax = rightMax
    elif rightPathSum == None:
        maxPathSum = leftPathSum
        rightPathSum = 0
        rightMax = leftMax
    else:
        maxPathSum = max(leftPathSum,rightPathSum)
    pathForParent = maxPathSum + tree.value
    pathWithChildren = leftPathSum + rightPathSum + tree.value
    return [pathForParent, max(maxPathSum,leftMax,rightMax,pathWithChildren)]
