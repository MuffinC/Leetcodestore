def lengthOfLIS(nums):
    dp = {len(nums)-1: 1}

    def dfs(index):
        if index in dp: return dp[index]

        # check if theres anything > cur
        for x in range(index, len(nums)):
            if nums[x] > nums[index]:
                dp[index] = max(1 + dp.get(x,1), dp.get(index,1))
        dp[index] =dp.get(index, 1)

        return

    for ind in range(len(nums)-1,-1,-1):

        dfs(ind )

    return max(dp.values())

print(lengthOfLIS([10,9,2,5,3,7,101,18]))