def zeroSumSubarray(nums):
    if nums == []:
        return False
    if 0 in nums or sum(nums) == 0:
        return True
    lstSum = [nums[0]]
    for i in range(1, len(nums)):
        lstSum.append(lstSum[-1] + nums[i])
    if 0 in lstSum or len(set(lstSum)) < len(nums):
        return True
    return False