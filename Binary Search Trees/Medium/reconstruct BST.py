class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def reconstructBst(preOrderTraversalValues):
    if preOrderTraversalValues == []:
        return None
    rootValue = preOrderTraversalValues.pop(0)
    root = BST(rootValue)
    if preOrderTraversalValues == []:
        return root
    leftArr = []
    while preOrderTraversalValues[0] < rootValue:
        leftArr.append(preOrderTraversalValues.pop(0))
        if preOrderTraversalValues == []:
            break
    rightArr = preOrderTraversalValues
    root.left = reconstructBst(leftArr)
    root.right = reconstructBst(rightArr)
    return root