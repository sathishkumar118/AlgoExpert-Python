# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def heightBalancedBinaryTree(tree):
    if heightBalanceChecker(tree) == -1:
        return False
    else:
        return True

def heightBalanceChecker(tree):
    if tree == None:
        return 0
    leftDepth = heightBalanceChecker(tree.left)
    rightDepth = heightBalanceChecker(tree.right)
    if leftDepth == -1 or rightDepth == -1:
        return -1
    if abs(leftDepth - rightDepth) > 1:
        return -1
    else:
        return max(leftDepth,rightDepth)+1
