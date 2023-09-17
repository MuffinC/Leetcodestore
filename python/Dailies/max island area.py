def maxAreaOfIsland(grid):
    rows, cols = len(grid), len(grid[0])

    def dfs(x, y):
        # x,y is the starting location , isl is the area of the island
        nonlocal cur
        if x < 0 or x >= rows or y < 0 or y >= cols or grid[x][y] != 1:
            return
        cur += 1
        grid[x][y] = '#'  # area is covered
        direction = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for d in direction:
            dfs(x + d[0], y + d[1])
        return


    total = cur= 0
    for x in range(rows):
        for y in range(cols):
            if grid[x][y] == 1:
                cur=0
                dfs(x, y)
                total = max(total, cur)

    return total

print(maxAreaOfIsland([[0,0,0,0,0,0,0,0]]))