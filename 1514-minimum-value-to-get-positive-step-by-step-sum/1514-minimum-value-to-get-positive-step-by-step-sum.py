class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        
        cur=[]
        start=0
        for x in nums:
            start+=x
            cur.append(start)
        print(cur)
        lowest=min(cur)
        if lowest<=0: 
            ans= (lowest*-1) +1
        elif lowest>1: ans=1
        else:ans=lowest
        
        return ans
        

