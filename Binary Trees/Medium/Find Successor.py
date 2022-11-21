# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def findSuccessor(tree, node):
    result,seen = inOrderTraverse(tree,node)
    return result

def inOrderTraverse(tree, node, result = None, seen = False):
    if tree == None or result != None:
        return result,seen
    else:
        result,seen = inOrderTraverse(tree.left, node, result, seen)
        if seen:
            if result == None:
                result = tree
            return result,seen
        if tree == node:
            seen = True
        return inOrderTraverse(tree.right, node, result, seen)
    pass
        
