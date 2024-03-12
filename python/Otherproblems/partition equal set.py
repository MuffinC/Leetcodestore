def canPartition(nums):
    cur = sorted(nums)
    l, r = 0, len(nums) - 1
    ltot, rtot = cur[l], cur[r]
    while l < r:
        if ltot == rtot:
            return True
        else:
            if ltot < rtot:
                l += 1
                ltot += cur[l]
            elif ltot > rtot:
                r -= 1
                rtot += cur[r]

    return False
print(canPartition([1,5,11,5]))