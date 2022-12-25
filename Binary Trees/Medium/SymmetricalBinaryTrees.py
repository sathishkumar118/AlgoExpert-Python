class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def inOrderTraversal(tree):
    if tree == None:
        return []
    return inOrderTraversal(tree.left) + [tree.value] + inOrderTraversal(tree.right)
def symmetricalTree(tree):
    return (tree.left == None and tree.right == None) or (inOrderTraversal(tree.left) == inOrderTraversal(tree.right)[::-1])
