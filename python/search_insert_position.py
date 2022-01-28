def searchInsert(nums, target):
    for x in range(0,len(nums),1):
        diff = nums[x] - target
        if(diff>=0):
            up=x
            break
        else:
            up =len(nums)
    return up






print(searchInsert([1,3,5,6],5))

