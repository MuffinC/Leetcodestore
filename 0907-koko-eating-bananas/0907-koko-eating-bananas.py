class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        res=r
        while l<=r:
            totalh = 0
            mid = (r + l) // 2

            for x in piles:
                totalh += math.ceil((x / mid))
            if totalh > h:
                l = mid+1
            else:
                #ans is somewhere on the left, time is acceptable
                res=min(res,mid)
                r = mid-1
        return res