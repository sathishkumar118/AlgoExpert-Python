def minHeightBst(array, root = None):
    root = BST(array.pop(int(len(array)/2)))
    while len(array) > 0:
        root.insert(array.pop(int(len(array)/2)))
    return root
    pass

"""def findDepth(BST):
    if BST == None:
        return 0
    return 1 + max(findDepth(BST.left),findDepth(BST.right))"""


class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
