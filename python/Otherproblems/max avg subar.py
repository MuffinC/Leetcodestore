def findMaxAverage(nums, k) :
    l, r = 0, k
    total = sum(nums[:k])
    mavg = total / k
    ans = mavg
    r-=1
    while r + 1 < len(nums):
        r += 1

        total += nums[r]
        total -= nums[l]
        l += 1
        if total / k > mavg:
            mavg = total / k
            ans = mavg

    return ans


print(findMaxAverage([1,12,-5,-6,50,3],4))