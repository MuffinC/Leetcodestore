def removeStars( s) :
    l = 0
    s = list(s)
    cur = []
    while l < len(s):
        if s[l] == '*' and cur:
            cur.pop()

        else:
            cur.append(s[l])
        l += 1

    return "".join(cur)

print(removeStars("leet**cod*e"))