def match(s,p):
    if len(s) != len(p): return False
    l = 0
    p = list(p)
    s = list(s)
    while l < len(s):
        if p[l] == s[l] or p[l] == '.':
            l += 1
            continue
        if l > 0 and p[l] == '*':
            if p[l - 1] == s[l] or p[l - 1] =='.':
                l += 1
                continue
            else:
                return False
        else:
            return False
    return True

print(match("aa",".*"))