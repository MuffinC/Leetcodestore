class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        if candidates*2<len(costs):
            minheap = costs[:candidates] + costs[len(costs) - candidates:]
        else: minheap=costs

        listleft = costs[:candidates]
        remainder = costs[candidates: len(costs) - candidates]
        ans = 0
        heapq.heapify(minheap)

        for x in range(k):
            val = heapq.heappop(minheap)
            ans += val
            if remainder:
                if val in listleft and len(remainder)>1:
                    cur=remainder[0]
                    heapq.heappush(minheap, cur)
                    listleft.remove(val)
                    remainder.pop(0)
                    listleft.append(cur)
                else:
                    heapq.heappush(minheap, remainder[-1])
                    remainder.pop(-1)

        return ans