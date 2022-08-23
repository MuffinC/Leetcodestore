def minSubArrayLen(target, nums):
    if sum(nums) < target: return 0
    mini = float("inf")
    L = 0
    # setting right
    total=0
    for x in range(len(nums)):
        total+=nums[x]
        while total>=target:
            mini=min(mini,x-L +1)
            total-=nums[L]
            L+=1
    return mini



print(minSubArrayLen(4,[1,4,4]))
