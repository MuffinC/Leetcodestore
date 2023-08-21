class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        ans = []
        potions.sort()
        for x in spells:
            l, r = 0, len(potions) - 1
            cur = 0
            #allclear
            if potions[0]*x>=success:
                ans.append(len(potions))
                continue
            #all fail
            elif potions[-1]*x<success:
                ans.append(0)
                continue
            #inbetween
            while l <= r:
                mid = l + ((r - l) // 2)
                if x*potions[mid-1] <success and x*potions[mid] >=success:
                    break
                elif x*potions[mid-1] >=success and x*potions[mid] >=success:
                    r=mid
                elif  x*potions[mid] < success:
                    l=mid+1

            cur=len(potions)-mid
            ans.append(cur)

        return ans
