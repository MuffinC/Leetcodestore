def isOneEditDistance(s, t):
    if s == t: return False
    t = list(t)
    s=list(s)
    for ind, letter in enumerate(s):
        if letter == t[ind]:
            continue
        else:

            if ind + 1 >= len(t):
                return False
            # insert
            elif s[ind:] == t[ind + 1:]:
                return True

            elif ind + 1 >= len(s):
                return False
            # remove
            elif s[ind + 1:] == t[ind:]:
                return True
            # swap
            elif s[ind + 1] == t[ind + 1]:
                return True
            else:
                return False

print(isOneEditDistance("ab","acb"))