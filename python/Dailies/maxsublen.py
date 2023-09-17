def maxSubArrayLen(nums, k) :
    if len(nums) == 1 and nums[0] == k: return 1
    elif len(nums) == 1 and nums[0] != k: return 0

    l, r = 0, len(nums) - 1
    tot = sum(nums)
    if tot == k: return len(nums)

    anslen = len(nums)

    while l < r:
        tot -= nums[l]
        if tot == k: return anslen - 1

        tot = tot + nums[l] - nums[r]
        if tot == k: return anslen - 1

        tot = tot - nums[l]
        l += 1
        r -= 1
        # if l<0 or r
        anslen -= 2

    # ans now can be 2 1 or 0
    if l != r:
        if nums[l] + nums[r] == k:
            return 2
        elif nums[l] == k or nums[r] == k:
            return 1
    else:
        if nums[l] == k: return 1
    return 0

print(maxSubArrayLen([-2,1,-3,4,-1,2,1,-5,4],0))