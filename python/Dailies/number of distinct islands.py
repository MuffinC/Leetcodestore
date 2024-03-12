def numDistinctIslands(grid):
    islands = set([])
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                islands.add(dfs(grid, i, j, "s"))

    return len(islands)


def dfs( g, i, j, path):
    if i < 0 or j < 0 or i >= len(g) or j >= len(g[i]) or g[i][j] == 0:
        return ""

    g[i][j] = 0
    return path \
           + dfs(g, i + 1, j, "d") + "u" \
           + dfs(g, i - 1, j, "u") + "d" \
           + dfs(g, i, j + 1, "r") + "l" \
           + dfs(g, i, j - 1, "l") + "r"
print(numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))