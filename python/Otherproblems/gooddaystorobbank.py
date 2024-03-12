def goodDaysToRobBank(security, time):
    n = len(security)

    decreasing = [0] * n
    consec = 0
    for i in range(1, n):
        if security[i] <= security[i - 1]:
            consec += 1
            decreasing[i] = consec
        else:
            consec = 0
            decreasing[i] = consec

    increasing = [0] * n
    consec = 0
    for i in range(n - 2, -1, -1):
        if security[i + 1] >= security[i]:
            consec += 1
            increasing[i] = consec
        else:
            consec = 0
            increasing[i] = consec

    ans = []
    for i in range(time, n - time):
        if increasing[i] >= time and decreasing[i] >= time:
            ans.append(i)
    return ans
print(goodDaysToRobBank([5,3,3,3,5,6,2],2))