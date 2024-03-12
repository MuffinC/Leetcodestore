def findMaxConsecutiveOnes(nums):
    pre, curr, maxlen = -1, 0, 0
    for n in nums:
        if n == 0:
            pre, curr = curr, 0
        else:
            curr += 1
        maxlen = max(maxlen, pre + 1 + curr)

    return maxlen


print(findMaxConsecutiveOnes([1,0,1,1,0]))