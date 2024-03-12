def solution(st):
    ans = 0
    while True:
        com = st[::-1]
        letter = 0
        for x in range(len(com)):
            if com[x] == '*' or com[x] == st[x] or st[x] == '*':
                letter += 1
            else:
                break
        if letter == len(com): return ans

        ans += 1
        st = st + '*'

    return ans

print(solution("abcdc"))