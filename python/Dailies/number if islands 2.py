def numIslands2(m, n, positions):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    ans = []
    rows, cols = m+1, n+1
    curt = 0
    hold = []
    for island in positions:
        swit = 0
        for dx, dy in directions:
            rx, ry = island[0] + dx, island[1] + dy
            if rx < 0 or ry < 0 or rx == rows or ry == rows: continue
            if [rx, ry] in hold:
                ans.append(curt)
                swit = 1

        hold.append(island)
        if swit == 1: continue
        curt += 1
        ans.append(curt)
    if curt < 0: return 0
    return ans

print(numIslands2(1,2,[[0,1],[0,0]]))