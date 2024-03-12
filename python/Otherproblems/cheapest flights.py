def findCheapestPrice(n, flights, src, dst, k) :
    import heapq
    minheap = []
    heapq.heapify(minheap)
    table = {}
    for flight in flights:
        if flight[0] not in table:
            table[flight[0]] = [[flight[2], flight[1]]]
        else:
            table[flight[0]].append([flight[2], flight[1]])

    ans = float("inf")
    if src not in table: return -1
    for flight in table[src]:
        heapq.heappush(minheap, [flight[0], flight[1], k])

    seen = set()
    seen.add(src)
    while minheap:

        price, node, kval = heapq.heappop(minheap)
        if node in seen or (kval <= 0 and node != dst): continue
        if node == dst:
            ans = min(ans, price)
            continue
        seen.add(node)
        if table.get(node,0) ==0: return -1
        for nx in table[node]:
            heapq.heappush(minheap, [nx[0] + price, nx[1], kval - 1])

    if ans == float("inf"): return -1
    return ans


print(findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],0,2,2))