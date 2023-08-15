def longestOnes(nums, k):
    l,mx=0,0
    #when u enumerate in array, its index and value
    for r,n in enumerate(nums):
        k-=(1-n)
        if k<0:
            k+=(1-nums[l])
            l+=1
        mx=max(mx,r-l+1)
    return mx
print(longestOnes([1,1,1,0,0,0,1,1,1,1,0],2))