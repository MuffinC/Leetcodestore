def pivotIndex(nums):
    if len(nums) == 1: return 0

    total = sum(nums)
    left = 0
    for x, y in enumerate(nums):
        if left == (total - left - y):
            return x
        left += y
    return -1


print(pivotIndex([1,7,3,6,5,6]))