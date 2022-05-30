strs = ["flower","flow","flight"]

result = ""
minimum = min(len(c) for c in strs)
for y in range(minimum):
    ch = strs[0][y]
    for x in strs:
        if ch != x[y]:
            return result
    result += ch
return result