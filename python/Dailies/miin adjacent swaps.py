def minimumSwaps(nums):
    smallest, maxi = min(nums), max(nums)
    if smallest == maxi: return 0

    mover = 0
    swaps = 0
    while nums[0] != smallest or nums[-1] != maxi:
        if mover + 1 < len(nums) and nums[mover] > nums[mover + 1]:
            hold = nums[mover]
            nums[mover] = nums[mover + 1]
            nums[mover + 1] = hold
            swaps += 1
        if mover == len(nums):
            mover = -1
        mover += 1
    return swaps

print(minimumSwaps([3,4,5,5,3,1]))