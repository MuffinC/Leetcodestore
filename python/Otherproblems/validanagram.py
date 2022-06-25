def isAnagram( s, t):

    if len(s)!=len(t): return False

    s=sorted(s)
    t=sorted(t)
    for x,y in enumerate(s):
        if y!=t[x]:
            return False
    return True


print(isAnagram("aacc","ccac"))