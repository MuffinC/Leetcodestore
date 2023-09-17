def networkDelayTime(times, n, k) -> int:
    # adj list?
    adj_list = defaultdict(list)

    for x, y, w in times:
        adj_list[x].append((w, y))

    visited = set()
    heap = [(0, k)]
    while heap:
        travel_time, node = heapq.heappop(heap)
        visited.add(node)

        if len(visited) == n:
            return travel_time

        for time, adjacent_node in adj_list[node]:
            if adjacent_node not in visited:
                heapq.heappush(heap, (travel_time + time, adjacent_node))

    return -1

print(networkDelayTime([[1,2,1],[2,3,2],[1,3,4]],3,1))