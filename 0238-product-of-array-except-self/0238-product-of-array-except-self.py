class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        total=1
        trigger=0
        zerocount=0
        for x in nums:
            if x ==0:
                trigger=1
                zerocount+=1

            else: total=total*x
        ans=[]                  
        for y in nums:
            if trigger ==0 and zerocount<1:
                ans.append(int(total/y))
            elif trigger==1 and y ==0 and zerocount<2:
                ans.append(total)
            else: ans.append(0)
        return ans
