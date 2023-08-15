def searchRange(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    def helper(nums,target,var):
        l,r=0,len(nums)-1
        ans=-1
        while l<=r:
            mid=l +(r-l) //2
            if nums[mid] == target:
                ans=mid
            if var =='low':
                if nums[mid]>= target:
                    r=mid-1
                else:
                    l=mid+1
            elif var =='high':
                if nums[mid] <=target:
                    l=mid+1
                else:
                    r=mid-1

        return ans


    ans= [-1,-1]
    ans[0]=helper(nums,target,'low')
    ans[1]=helper(nums,target,'high')




    return ans


print(searchRange([5,7,7,8,8,10],8))