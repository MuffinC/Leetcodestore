def canJump(nums):
    goalpost = len(nums) - 1
    for x in range(len(nums) - 1, -1, -1):
        # checking if goalpost can be shifted
        if x + nums[x] >= goalpost:
            goalpost = x

    return True if goalpost == 0 else False




print(canJump([2,3,2,0,4]))