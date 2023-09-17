class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        swaps=0
        maxi,mini=float("-inf"),float("inf")
        
        for x,y in enumerate(nums):
            if y>=maxi:
                maxi=y
                maxind=x
            if y<mini:
                mini=y
                miniind=x
        #no swaps required
        if (miniind == 0 and maxind==len(nums)-1) or len(nums)<2: 
            return 0
        #now we check if the indexes are not inbetween
        if miniind<maxind: return (miniind)+(len(nums)-1 -maxind)
        #now whatever is left is an overlapping situation, which at the very most will only result in a -1 effect on the other side
        return (miniind)+ (len(nums)-1-(maxind+1))

