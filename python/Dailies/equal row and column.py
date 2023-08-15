from collections import Counter


def equalPairs(grid) :
    tpse = Counter(zip(*grid))  # <-- determine the transpose
    #     and hash the rows

    grid = Counter(map(tuple, grid))  # <-- hash the rows of grid. (Note the tuple-map, so
    #     we can compare apples w/ apples in next step.)
    for t in tpse:
        print(t)
    return sum(tpse[t] * grid[t] for t in tpse)  # <-- compute the number of identical pairs

print(equalPairs([[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]))