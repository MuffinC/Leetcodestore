def minLengthAfterRemovals(nums):
    import bisect
    n = len(nums)
    i = nums[n // 2]
    print(bisect.bisect_right(nums, i))
    print(bisect.bisect_left(nums, i))
    cnt = bisect.bisect_right(nums, i) - bisect.bisect_left(nums, i)
    return max(n % 2, 2 * cnt - n)

print(minLengthAfterRemovals([1,3,4,9]))