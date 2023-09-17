def nearestExit(maze, entrance) :
    ans = float("inf")
    exits = []
    rows, cols = len(maze), len(maze[0])
    seen= set()
    def searcher(curpos, steps):
        steps += 1
        nonlocal ans, entrance
        if tuple(curpos) in seen or curpos[0]<0 or curpos[0]==rows or curpos[1]<0 or curpos[1]==cols or maze[curpos[0]][curpos[1]] == '+' :
            return
        elif (curpos != entrance) and (curpos[0] == 0 or curpos[0] == rows - 1 or curpos[1] == 0 or curpos[1] == cols - 1):
            ans=min(ans,steps)
            return
        seen.add(tuple(curpos))

        # we check up down left right
        searcher([curpos[0] + 1, curpos[1]], steps)
        searcher([curpos[0] - 1, curpos[1]], steps)
        searcher([curpos[0], curpos[1] + 1], steps)
        searcher([curpos[0], curpos[1] - 1], steps)

        return
    searcher(entrance, -1)

    if ans == float("inf"): return -1
    return ans

print(nearestExit([["+",".","+","+","+","+","+"],["+",".","+",".",".",".","+"],["+",".","+",".","+",".","+"],["+",".",".",".",".",".","+"],["+","+","+","+",".","+","."]],[0,1]))