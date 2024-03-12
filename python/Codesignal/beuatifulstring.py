def solution(inputString):
    from collections import Counter
    table = Counter(inputString)
    cur = []
    for x, y in table.items():
        cur.append((x, y))
    cur = sorted(cur)
    if cur[0][0] != 'a': return False

    start = ord('a') + 1
    numstart = cur[0][1]
    for x, y in cur[1:]:
        if ord(x) != start: return False
        if y < numstart: numstart = y
        if y> numstart:return False
        start += 1
    return True


print(solution("aabbb"))