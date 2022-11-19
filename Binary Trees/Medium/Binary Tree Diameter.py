""" A method that takes in a binary tree and returns its length of the longest path.
"""
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def binaryTreeDiameter(tree):
    # Write your code here.
    return newBinaryTreeDiameter(tree)[0]-1
    #return -1

def newBinaryTreeDiameter(tree, maxLen = 0):
    if tree == None:
        return maxLen,0
    elif tree.left == None and tree.right == None:
        return max(maxLen,1),1
    else:
        leftLen = newBinaryTreeDiameter(tree.left,maxLen)
        rightLen = newBinaryTreeDiameter(tree.right,maxLen)
        currLen = leftLen[1] + rightLen[1] + 1
        return max(maxLen,leftLen[0],rightLen[0],currLen),max(leftLen[1] + 1,rightLen[1] + 1)