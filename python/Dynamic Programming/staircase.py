def climbStairs(n,memo={}):
    if n in memo: return memo[n]
    if n==0: return 1
    if n<0: return None
    steps=[1,2]
    ans=0
    for x in steps:
        res=climbStairs(n-x,memo)

        if (res):
            ans+=res
    memo[n]=ans

    return ans







print(climbStairs(35))