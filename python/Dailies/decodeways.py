def numDecodings(s):
    dp = {len(s): 1}

    def dfs(i):
        if i in dp:
            return dp[i]
        if s[i] == "0":
            return 0
        res = dfs(i + 1)
        if ((i + 1) < len(s) and (s[i] == "1" or s[i] == "2" and s[i + 1] in "0123456")):
            # if it starts with 1 you can create a dooouble digit balue
            res += dfs(i + 2)
        dp[i] = res
        return res

    return dfs(0)


print(numDecodings("226"))