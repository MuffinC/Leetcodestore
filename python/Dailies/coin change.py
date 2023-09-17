def coinChange(coins, amount):
    ans = float("inf")
    seen=set()
    def dfs(cur, coinc):
        nonlocal ans,seen
        if cur > amount:
            return False
        if cur == amount:
            ans = min(ans, coinc)
            return True

        for x in coins:

            if dfs(cur + x, coinc + 1):
                break

    dfs(0, 0)
    if ans ==float("inf"): return -1
    return ans

print(coinChange([1,2,5],11))