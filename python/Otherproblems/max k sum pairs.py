def maxOperations(nums, k):
    ans = 0
    table = {}
    for x in nums:
        if x not in table:
            table[x] = 1
        else:
            table[x] += 1
    seen = set()
    for x in nums:
        if x not in seen and (k - x) in table:
            if x == (k - x):
                ans += table[x] // 2
            else:
                ans += min(table[x], table[k - x])
            seen.add(x)
            seen.add(k - x)

    return ans


print(maxOperations([4,4,1,3,1,3,2,2,5,5,1,5,2,1,2,3,5,4],2))