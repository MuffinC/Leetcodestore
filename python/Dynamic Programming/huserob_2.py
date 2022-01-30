def rob(nums):
    if len(nums)<=1:
        return nums[0]
    elif  len(nums)== 2:
        return max(nums[0], nums[1])
    else:
        robbed = [nums[0], max(nums[1], nums[0])]

        for i in range(2, len(nums)):
            robbed.append(max((robbed[i - 2] + nums[i]), robbed[i - 1]))

        return (robbed[-1])
print(rob([1,2,3]))