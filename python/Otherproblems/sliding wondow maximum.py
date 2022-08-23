def maxSlidingWindow( nums, k):
    if len(nums) == k: return [max(nums[::])]
    if k==1: return nums
    res = []
    stack=[]
    l=0

    for r in range(k-1,len(nums)):
        if not stack:
            stack=list(reversed(sorted(nums[l:r+1])))


        else:
            while stack and nums[r]>stack[0]:
                stack.pop(0)
            stack.insert(0,nums[r])
        res.append(stack[0])
        l+=1
        stack.pop(0)
    return res





print(maxSlidingWindow([1,3,-1,-3,5,3,6,7],3))