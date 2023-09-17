def findAnagrams(s, p):
    from collections import Counter
    pco = Counter(p)
    pcur = Counter(p)
    ans = []
    l, r = 0, 0
    while l < len(s) and r < len(s):
        if s[r] in pco and pco[s[r]] > 0:
            pco[s[r]] -= 1
            r += 1
            if sum(pco.values()) == 0:
                ans.append(l)
                pco[s[l]] += 1
                l += 1
        elif s[r] not in pco:
            pco = pcur
            l = r
            r += 1

    return ans
print(findAnagrams("cbaebabacd","abc"))