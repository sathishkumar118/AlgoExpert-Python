# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def validateBst(tree):
    # Write your code here.
    if tree != None:
        if tree.left == None and tree.right == None:
            return True
        elif tree.left == None:
            if tree.value <= findMin(tree.right):
                return validateBst(tree.right)
            else:
                return False
        elif tree.right == None:
            if tree.value > findMax(tree.left):
                return validateBst(tree.left)
            else:
                return False
        else:
            if tree.value > findMax(tree.left) and tree.value <= findMin(tree.right):
                return validateBst(tree.left) and validateBst(tree.right)
            else:
                return False
def findMax(tree):
    if tree.right == None:
        return tree.value
    else:
        return max(tree.value,findMax(tree.right))
def findMin(tree):
    if tree.left == None:
        return tree.value
    else:
        return min(tree.value,findMin(tree.left))