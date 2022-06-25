def isIsomorphic( s, t):
    holder = {}
    for x, y in enumerate(s):
        if y not in holder.keys() and t[x] not in holder.values():
            holder[y] = t[x]
        elif y in holder.keys() and t[x] == holder[y]:
            continue
        else:
            return False
    return True


print(isIsomorphic("bbbaaaba","aaabbbba"))