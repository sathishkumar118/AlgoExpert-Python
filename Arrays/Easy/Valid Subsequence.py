def isValidSubsequence(array, sequence):
    # Write your code here.
	it = 0
	for item in array:
		if item == sequence[it]:
			if it == len(sequence) - 1: return True
			else: it += 1
	return False
	pass