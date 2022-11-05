def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)<=1: return len(nums)
    mover=0
    while mover+1<len(nums):
        if nums[mover] == nums[mover+1] and mover+1<len(nums):
            nums.pop(mover)
        else:
            mover+=1
    return mover+1





print(removeDuplicates([1,1,2]))