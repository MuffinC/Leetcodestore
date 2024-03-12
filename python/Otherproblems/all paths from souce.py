def allPathsSourceTarget(graph) :
    # adj list
    from collections import defaultdict
    table = defaultdict()
    x = 0
    for paths in graph:
        table[x] = paths
        x += 1
    ans = []
    seen = set()

    def dfs(curnode, path):
        nonlocal ans
        if curnode == len(graph) - 1:
            path.append(curnode)
            ans.append(path.copy())
            path.pop()
            return

        if curnode in seen: return

        path.append(curnode)
        seen.add(curnode)
        for next in table[curnode]:
            dfs(next, path)

            seen.discard(next)
        path.pop()


    dfs(0, [])
    return ans


print(allPathsSourceTarget([[1,2],[3],[3],[]]))