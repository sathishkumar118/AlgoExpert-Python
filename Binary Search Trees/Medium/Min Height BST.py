def minHeightBst(array):
    if array == []:
        return None
    midIdx = int(len(array)/2)
    leftArr = array[:midIdx]
    rightArr = array[midIdx:]
    root = BST(rightArr.pop(0))
    root.left = minHeightBst(leftArr)
    root.right = minHeightBst(rightArr)
    return root

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