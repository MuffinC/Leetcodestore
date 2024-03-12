def findMaximizedCapital(k, w, profits, capital):
    hold = []
    for ind in range(0, len(profits)):
        hold.append((profits[ind], capital[ind]))
    hold = sorted(hold, reverse=True)

    while k > 0:
        for x in range(len(hold)):
            if w >= hold[x][1]:
                w += hold[x][0]
                hold.pop(x)
                k -= 1
                break
    return w

print(findMaximizedCapital(1,0,[1,2,3],[1,1,2]))