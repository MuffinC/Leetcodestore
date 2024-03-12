def minIncrementForUnique(nums):
    nums = sorted(nums)
    ans = 0
    for x in range(1, len(nums)):
        if nums[x] <= nums[x - 1]:
            diff = abs(nums[x] - nums[x - 1]) + 1
            ans += diff
            nums[x] = nums[x]+diff
    return ans


print(minIncrementForUnique([3,2,1,2,1,7]))