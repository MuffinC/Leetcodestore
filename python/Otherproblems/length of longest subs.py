def lengthOfLongestSubsequence(nums, target):
    anslen = -1

    def bfs(curlist, ind):
        nonlocal anslen
        if sum(curlist) == target:
            anslen = max(anslen, len(curlist))
            return
        if sum(curlist) > target or ind >= len(nums) or tuple(curlist) in seen:
            return

        seen.add(tuple(curlist))

        for y in range(1, len(nums)):
            if ind + y >= len(nums): break
            curlist.append(nums[ind + y])
            bfs(curlist, y + ind)
            curlist.pop()

        return

    seen = set()
    for i, x in enumerate(nums):
        bfs([x], i )

    return anslen

print(lengthOfLongestSubsequence([4,1,3,2,1,5],7))