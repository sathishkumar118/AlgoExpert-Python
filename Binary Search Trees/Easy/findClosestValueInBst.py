""" A function that fetches the closest value present in the BST based on the given target.
"""
def findClosestValueInBst(tree, target):
    # Write your code here.
	if target > tree.value and tree.right:
		right_diff = findClosestValueInBst(tree.right, target)
		if abs(right_diff - target) < abs(tree.value - target):
			return right_diff
	elif target < tree.value and tree.left:
		left_diff = findClosestValueInBst(tree.left, target)
		if abs(left_diff - target) < abs(tree.value - target):
			return left_diff
	return tree.value
    pass


# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
