from collections import deque
def wallsAndGates(rooms):
    """
    Do not return anything, modify rooms in-place instead.
    """
    rows, cols = len(rooms), len(rooms[0])
    # iterate through and record the gates
    gates = deque()
    for x in range(rows):
        for y in range(cols):
            if rooms[x][y] == 0:
                gates.append((x, y))

    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    dist = 1
    while gates:
        curx, cury = gates.popleft()
        for dx, dy in directions:
            row, col = curx + dx, cury + dy
            if row < 0 or col < 0 or row >= rows or col >= cols or rooms[row][col] != 2147483647:
                continue
            rooms[row][col] = rooms[curx][cury]+1
            gates.append((row, col))

    return rooms


print(wallsAndGates([[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]))