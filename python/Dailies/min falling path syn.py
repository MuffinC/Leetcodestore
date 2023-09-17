def minFallingPathSum( matrix):
    ans = float("inf")
    rows, cols = len(matrix), len(matrix[0])
    directions = [(1, 0), (1, 1), (1, -1)]

    def dfs(x, y):
        nonlocal cur, ans
        if x < 0 or y < 0 or x >= rows or y >= cols:
            return
        if x == rows - 1:
            cur += matrix[x][y]
            ans = min(ans, cur)
            cur -= matrix[x][y]
            return
        cur += matrix[x][y]

        for d in directions:
            curx, cury = x + d[0], y + d[1]
            dfs(curx, cury)
        cur -= matrix[x][y]
        return

    for y in range(cols):
        cur = 0
        dfs(0, y)


    return ans

print(minFallingPathSum([[-19,57],[-40,-5]]))

