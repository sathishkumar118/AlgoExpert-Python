"""
Methods which traverses through the BST in three different ways :- inorder traversal, preorder traversal and postorder traversal
"""
def inOrderTraverse(tree, array):
    # Write your code here.
    if tree == None:
        return array
    else:
        array = inOrderTraverse(tree.left,array)
        array.append(tree.value)
        array = inOrderTraverse(tree.right,array)
        return array
    pass

def preOrderTraverse(tree, array):
    # Write your code here.
    if tree == None:
        return array
    else:
        array.append(tree.value)
        array = preOrderTraverse(tree.left, array)
        array = preOrderTraverse(tree.right, array)
        return array
    pass


def postOrderTraverse(tree, array):
    # Write your code here.
    if tree == None:
        return array
    else:
        array = postOrderTraverse(tree.left, array)
        array = postOrderTraverse(tree.right, array)
        array.append(tree.value)
        return array
    pass
