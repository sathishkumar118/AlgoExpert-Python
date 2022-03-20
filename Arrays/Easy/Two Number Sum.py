def twoNumberSum(array, targetSum):
    # Write your code here.
	for i in range(len(array)):
		try:
			return [array[i],array[array.index(targetSum-array[i],i+1)]]
		except:
			continue
	return []
    pass