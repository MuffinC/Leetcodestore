def maxFrequency(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    nums.sort()
    l, r = 0, 0
    ans,total=0,0
    while r<len(nums):
        total+=nums[r]
        #(r-l+1) is just the window length
        while nums[r] *(r-l+1)> total+k:
            total-=nums[l]
            l+=1
        ans=max(ans,r-l+1)
        r+=1


    return ans

print(maxFrequency([1,2,4],5))