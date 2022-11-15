""" A method which takes in a binary tree and returns the inverted binary tree
"""
def invertBinaryTree(tree):
    # Write your code here.
    if tree == None:
        return tree
    else:
        leftSubTree = invertBinaryTree(tree.left)
        rightSubTree = invertBinaryTree(tree.right)
        tree.left = rightSubTree
        tree.right = leftSubTree
        return tree
    pass


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
