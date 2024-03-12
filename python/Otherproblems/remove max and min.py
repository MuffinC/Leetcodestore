def minimumDeletions(nums):
    if len(nums) == 1: return 1
    top, bot = max(nums), min(nums)
    restop, rebot = "", ""
    ans = 0
    for ind, x in enumerate(nums):
        if x == top:
            if ind + 1 < len(nums) - ind:
                cur1 = ind + 1
                restop = 'L'
            else:
                cur1 = len(nums) - ind
                restop = 'R'
        elif x == bot:
            if ind + 1 < len(nums) - ind:
                cur2 = ind + 1
                rebot = 'L'
            else:
                cur2 = len(nums) - ind
                rebot = 'R'
    if rebot != restop:
        ans += cur1 + cur2
    else:
        ans += max(cur1, cur2)
    return ans

print(minimumDeletions([-1,-53,93,-42,37,94,97,82,46,42,-99,56,-76,-66,-67,-13,10,66,85,-28]))