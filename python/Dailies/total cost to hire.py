import heapq
def totalCost(costs, k, candidates):
    if candidates * 2 < len(costs):
        minheap = costs[:candidates] + costs[len(costs) - candidates:]
    else:
        minheap = costs

    listleft = costs[:candidates]
    remainder = costs[candidates: len(costs) - candidates]
    ans = 0
    heapq.heapify(minheap)

    for x in range(k):
        val = heapq.heappop(minheap)
        ans += val
        if remainder:
            if val in listleft and len(remainder) > 1:
                cur = remainder[0]
                heapq.heappush(minheap, cur)
                listleft.remove(val)
                remainder.pop(0)
                listleft.append(cur)
            else:
                heapq.heappush(minheap, remainder[-1])
                remainder.pop(-1)

    return ans

print(totalCost([50,80,34,9,86,20,67,94,65,82,40,79,74,92,84,37,19,16,85,20,79,25,89,55,67,84,3,79,38,16,44,2,54,58],7,12))