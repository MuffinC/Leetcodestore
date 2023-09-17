def maxProduct(nums):
    ans = float("-inf")

    def rec(cur, i):
        nonlocal ans

        cur = cur * nums[i]
        i += 1

        ans = max(ans, cur)
        if i >= len(nums):
            return
        for x in range(i, len(nums)):
            rec(cur, x)

    rec(1, 0)

    return ans

print(maxProduct([2,3,-2,4]))