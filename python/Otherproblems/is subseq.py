def isSubsequence( s: str, t: str) -> bool:
    s = list(s)
    for x in t:
        if x == s[0]:
            s.pop(0)
    if s == 0: return True
    return False
print(isSubsequence("abc","ahbgdc"))