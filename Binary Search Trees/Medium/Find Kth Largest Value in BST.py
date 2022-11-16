"""find the Kth largest value in given BST
"""

class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def findKthLargestValueInBst(tree, k):
    # Write your code here.
    return reverseOrderTraverse(tree, [])[k-1]

def reverseOrderTraverse(tree, array):
    # Write your code here.
    if tree == None:
        return array
    else:
        array = reverseOrderTraverse(tree.right,array)
        array.append(tree.value)
        array = reverseOrderTraverse(tree.left,array)
        return array
    pass