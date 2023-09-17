def getPrefixScores(arr):
    # Write your code here

    """
    [1 2 3]
    [1 3 6]

    [1 2 3 4 5]
    [1+5, 2+1+5, 3+2+1+5]

    """
    ans = [arr[0] + arr[0]]
    dp = [arr[0]]
    maxn = arr[0]
    x=1
    for y in arr[1:]:
        if y > maxn:
            maxn = y
        dp.append(y + dp[x - 1])
        res = sum(dp) + len(dp) * maxn
        ans.append(res)
        x+=1

    return ans

print(getPrefixScores([1,2,1]))