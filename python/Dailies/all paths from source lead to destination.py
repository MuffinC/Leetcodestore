def leadsToDestination(n, edges, source, destination):
    # adj list
    table = {x: [] for x in range(n)}

    for nodes in edges:
        table[nodes[0]].append(nodes[1])
    seen = set()

    def dfs(node):
        if not table[node] or node in seen: return False

        if node == destination: return True

        seen.add(node)
        while table[node]:
            nnode = table[node].pop()
            if dfs(nnode): return True
        return False
    tot=len(table[source])
    checker=0
    for x in table[source]:
        seen=set()
        if dfs(x):checker +=1
    if checker==tot: return True
    return False

print(leadsToDestination(3,[[0,1],[1,1],[1,2]],0,2))