def validTree(n, edges):
    # adjacency list + seen set
    # 0:1

    adjlist = {x: [] for x in range(n)}
    for x in edges:
        adjlist[x[0]].append(x[1])


    seen = set()

    def dfs(cur):
        if cur in seen:
            return False
        if not adjlist[cur]:
            return True
        seen.add(cur)
        for y in adjlist[cur]:
            if not dfs(y): return False
            if dfs(y):
                adjlist[cur].remove(y)
        seen.remove(cur)
        return True

    for x in range(n):
        if not dfs(x): return False
    return True

print(validTree(5,[[0,1],[1,2],[2,3],[1,3],[1,4]]))

