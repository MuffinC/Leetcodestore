def minimumOperations(nums):
    l, r = 0, len(nums) - 1
    ops = 0
    while l < r:
        if nums[l] == nums[r]:
            l += 1
            r -= 1
        elif nums[l] < nums[r] and l + 1 < len(nums):
            # right is more than left
            hold = nums.pop(l + 1)
            nums[l] = nums[l] + hold
            r-=1
            ops += 1
        elif nums[r] < nums[l] and r - 1 >= 0:
            # left is more
            hold = nums.pop(r)
            r-=1
            nums[r] = nums[r] + hold
            ops += 1

    return ops

print(minimumOperations([1,2,3,4]))