def nearestExit(maze, entrance) :
    import heapq
    ans = float("inf")
    rows, cols = len(maze), len(maze[0])
    minheap = []
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    seen = set()

    def dfs(steps, x, y):
        nonlocal ans
        if x < 0 or x == rows or y < 0 or y == cols or maze[x][y] == '+' or (x, y) in seen:
            return False
        if [x,y] != entrance and (x == 0 or y == 0 or x == rows - 1 or y == cols - 1):
            ans = min(ans, steps)
            return True
        seen.add((x, y))
        for rx, ry in directions:
            dx, dy = rx + x, ry + y
            heapq.heappush(minheap, (steps + 1, dx, dy))
        while minheap:
            step1, x1, y1 = heapq.heappop(minheap)
            if dfs(step1, x1, y1): return True
        return False

    if dfs(0, entrance[0], entrance[1]): return ans
    return -1

print(nearestExit([["+","+","+"],[".",".","."],["+","+","+"]],[1,0]))