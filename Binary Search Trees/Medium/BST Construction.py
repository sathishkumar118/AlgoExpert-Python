"""
Write a BST class for binary search tree with add,remove and contains methods.
"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if value >= self.value:
            #go right
            if self.right == None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            #go left
            if self.left == None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        return self

    def contains(self, value):
        # Write your code here.
        if self.value == value:
            return True
        elif value > self.value:
            if self.right == None:
                return False
            else:
                return self.right.contains(value)
        else:
            if self.left == None:
                return False
            else:
                return self.left.contains(value)
        pass

    def remove(self, value):
        # Write your code here.
        # Do not edit the return statement of this method.
        if self.contains(value):
            if self.value == value and self.right == None and self.left == None:
                return self
            else:
                self.remove_actual(value)
    def remove_actual(self, value):
        if self.value == value:
            if self.right == None and self.left == None:
                return None
            elif self.right == None:
                self.value = self.left.value
                self.left = self.left.left
                return self
            elif self.left == None:
                self.value = self.right.value
                self.right = self.right.right
                return self
            parent = self
            leftMost = self.right
            while leftMost.left != None:
                parent = leftMost
                leftMost = leftMost.left
            leftMostValue = leftMost.value
            if leftMost.right != None:
                leftMost.value = leftMost.right.value
                leftMost.right = leftMost.right.right
            else:
                if parent == self:
                    parent.right = None
                else:
                    parent.left = None
            self.value = leftMostValue
        elif self.value < value and self.right != None:
            self.right = self.right.remove_actual(value)
        elif self.value > value and self.left != None:
            self.left = self.left.remove_actual(value)
        return self
        pass
