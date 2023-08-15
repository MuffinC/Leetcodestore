def minSubArrayLen(target, nums) :
    l, r = 0, 0
    res = 10 ** 9
    total = 0
    counter = 0
    exist = False
    while l < len(nums):
        if total < target and r < len(nums):
            total += nums[r]
            counter += 1
            r += 1

        elif total >= target:
            exist = True
            res = min(res, counter)
            total -= nums[l]
            counter -= 1
            l += 1
        if total < target and r == len(nums):
            break
    if exist == False: return 0
    return res
print(minSubArrayLen(7,[2,3,1,2,4,3]))