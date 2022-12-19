def largestNumber(nums):
    """
    :type nums: List[int]
    :rtype: str
    """
    if len(nums) <= 1: return str(nums[0])
    cur = str(nums[0])
    nums=sorted(nums)
    for x in range(1, len(nums)):
        cur = max(int(str(nums[x]) + cur), int(cur + str(nums[x])))
        cur = str(cur)
    return cur


print(largestNumber([10,2,9,39,17]))