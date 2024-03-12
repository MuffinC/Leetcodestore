def maxDistance(grid) :
    import heapq
    ans = 0
    rows, cols = len(grid), len(grid[0])
    seen = set()
    minheap = []
    heapq.heapify(minheap)

    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                seen.add(tuple((x, y)))
                heapq.heappush(minheap, [0, tuple((x, y))])

    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    while minheap:
        steps, cur = heapq.heappop(minheap)
        x, y = cur[0], cur[1]
        for dx, dy in directions:
            rx, ry = dx + x, dy + y
            if tuple((rx, ry)) in seen or rx < 0 or ry < 0 or rx >= rows or ry >= cols: continue
            seen.add(tuple((rx, ry)))
            heapq.heappush(minheap, [steps+1, tuple((rx, ry))])
            ans = max(ans, steps+1)

    if ans == 0: return -1
    return ans

print(maxDistance([[1,0,1],[0,0,0],[1,0,1]]))