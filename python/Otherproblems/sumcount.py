def sumCounts(nums) :
    diff = 1
    ans = 0
    while True:
        if diff >= len(nums): break
        for l in range(0, len(nums)):
            if l+diff> len(nums):break
            curlist = nums[l:l + diff]
            ans += (len(set(curlist)) ** 2)
        diff += 1

    ans += (len(set(nums)) ** 2)
    return ans

print(sumCounts([1,2,1]))