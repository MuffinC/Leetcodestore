def mincostTickets( days, costs):
    """
    :type days: List[int]
    :type costs: List[int]
    :rtype: int
    """
    # the cache
    dp = {}

    def dfs(i):
        if i == len(days): return 0
        if i in dp: return dp[i]

        # set default value
        dp[i] = float("inf")
        for d, c in zip([1, 7, 30], costs):
            # need to find an out of bounds date
            j = i
            while j < len(days) and days[j] < days[i] + d:
                j += 1
            dp[i] = min(dp[i], c + dfs(j))
        return dp[i]

    return dfs(0)

print(mincostTickets([1,4,6,7,8,20], [2,7,15]))