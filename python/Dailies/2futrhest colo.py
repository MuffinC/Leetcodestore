def maxDistance(colors):
    l, r = 0, len(colors) - 1
    ans = float("-inf")
    while l < len(colors):
        if colors[r] != colors[l]:
            ans = max(ans, r - l)
        if r <= l:
            l += 1
            r = len(colors) - 1
            continue
        r -= 1
    return ans

print(maxDistance([1,1,1,6,1,1,1]))