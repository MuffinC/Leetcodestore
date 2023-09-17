def mostPoints(questions):
    dp = {}

    def dfs(i):
        if i >= len(questions): return 0
        if i in dp: return dp[i]

        dp[i] = max(dfs(i + 1), questions[i][0] + dfs(i + 1 + questions[i][1]))
        return dp[i]

    return dfs(0)
print(mostPoints([[21,5],[92,3],[74,2],[39,4],[58,2],[5,5],[49,4],[65,3]]))