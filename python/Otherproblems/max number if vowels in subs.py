def maxVowels(s, k) :
    vowels = ['a', 'e', 'i', 'o', 'u']
    ans = 0
    res = 0

    for x in range(0, k):
        if s[x] in vowels:
            ans += 1
    l, r = 0, k - 1
    res = max(ans, res)

    for x in range(k, len(s)):
        if s[x] in vowels:
            ans += 1
        if s[x-k] in vowels:
            ans -= 1
        res = max(res, ans)

    return res

print(maxVowels("abciiidef",  3))