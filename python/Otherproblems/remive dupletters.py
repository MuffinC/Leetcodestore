def removeDuplicateLetters(s):
    res = []
    for x in s:
        if x not in res:
            res.append(x)
    ans = "".join(res)
    return ans
print(removeDuplicateLetters("bcabc"))