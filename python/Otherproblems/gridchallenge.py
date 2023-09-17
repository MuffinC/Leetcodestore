def gridChallenge(grid):
    # Write your code here
    table = []
    for ind, word in enumerate(grid):
        table.append(list(sorted(list(word))))

    rows, cols = len(table), len(table[0])

    for c in range(0, cols):
        for r in range(0, rows):
            if (r, c) == (0, 0):
                continue
            elif table[r][c] >= table[r - 1][c]:
                continue
            else: return "NO"
    return "YES"

print(gridChallenge(['eabcd','fghij','olkmn','trpqs','xywuv']))