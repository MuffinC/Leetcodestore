def solve(board):
    """
    Do not return anything, modify board in-place instead.
    """
    rows, cols = len(board), len(board[0])
    # run a searcher from the borders
    borders = set()
    seen = set()
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(x, y):
        if x < 0 or x >= rows or y < 0 or y >= cols or board[x][y] == "X" or (x, y) in seen:
            return
        if board[x][y] == "O":
            borders.add((x, y))
            seen.add((x, y))
            for d in directions:
                dfs(x + d[0], y + d[1])

    x = 0
    for y in range(0, cols):
        dfs(x, y)
    x = rows - 1
    for y in range(0, cols):
        dfs(x, y)
    y = 0
    for x in range(0, rows):
        dfs(x, y)
    y = cols - 1
    for x in range(0, rows):
        dfs(x, y)

    for x in range(rows):
        for y in range(cols):
            if (x, y) not in borders and board[x][y] == "O":
                board[x][y] = "X"



print(solve([["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))