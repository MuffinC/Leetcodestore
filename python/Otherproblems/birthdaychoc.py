def birthday(s, d, m):
    # Write your code here
    if len(s) == 1 and s[0] == d:
        return 1
    elif len(s) == 1 and s[0] != d:
        return 0

    l, r = 0, m
    tot = sum(s[:m])
    ans = 0

    while r < len(s):
        if tot == d: ans += 1
        tot -= s[l]
        tot += s[r]
        r += 1
        l += 1
    if tot == d: ans += 1
    return ans

print(birthday([2, 5, 1, 3, 4, 4, 3 ,5 ,1, 1, 2, 1, 4, 1, 3, 3, 4, 2, 1],18,7))