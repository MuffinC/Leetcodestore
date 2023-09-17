class Solution:
    def minSwaps(self, data: List[int]) -> int:
        l,r=0, sum(data)
        zeros = minSwaps = len(data[:r]) - sum(data[:r])
        for i in range(r, len(data)):
            if data[i - r] == 0:
                zeros -= 1
            
            if data[i] == 0:
                zeros += 1
            minSwaps = min(minSwaps, zeros)
        return minSwaps
        


        return minSwaps
        