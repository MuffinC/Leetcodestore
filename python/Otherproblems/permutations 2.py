def permuteUnique(nums):
    ans = []
    seen = set()

    def dfs(curlist):
        if tuple(curlist) in seen:
            return
        if len(curlist) == tot:
            seen.add(tuple(curlist))
            ans.append(curlist.copy())
            return
        tot2 = len(nums)
        for y in range(tot2):
            cur = nums.pop(y)
            curlist.append(cur)
            dfs(curlist)
            curlist.pop()
            nums.insert(y,cur)
        return

    tot = len(nums)
    for x in range(tot):
        cur = nums.pop(x)
        dfs([cur])
        nums.insert(x,cur)
    return ans


print(permuteUnique([1,1,2]))
