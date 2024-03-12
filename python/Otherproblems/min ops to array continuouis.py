def minOperations(nums):
    import sys
    import bisect

    n = len(nums)
    nums = sorted(set(nums))
    ans = sys.maxsize

    for i, s in enumerate(nums):
        e = s + n - 1
        idx = bisect.bisect_right(nums, e)

        ans = min(ans, n - (idx - i))
    return ans

print(minOperations([1,10,100,1000]))