def minSwaps(s):
    """
    :type s: str
    :rtype: int
    """
    ref = []
    maxi, cur = 0, 0
    for x in s:
        if x == "[":
            cur += 1
        else:
            cur -= 1
        maxi = max(maxi, cur)
    return maxi + 1 / 2

print(minSwaps("][]["))