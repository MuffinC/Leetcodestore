def sortArray(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) == 1: return nums
    # insertion sort, first digit is already sorted
    for x in range(1, len(nums)):
        val = nums[x]
        nums[x] = '*'  # create the hole
        hole = x

        while nums[hole] == '*':
            if nums[hole - 1] > val and hole-1>=0:

                nums[hole] = nums[hole - 1]
                hole -= 1
                nums[hole] = '*'
            else:
                nums[hole] = val
    return nums

print(sortArray([5,2,3,1]))