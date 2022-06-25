def productExceptSelf(nums):
    res=1
    trigger=0

    for k in nums:
        if k==0:
            trigger+=1
        else:res=res*k

    ans=[0]*len(nums)
    if trigger>1: return ans

    for x,y in enumerate(nums):
        if y==0:
            ans[x]=res
        elif trigger==1:
            ans[x]=0
        else:
            ans[x]=int(res/y)
    return ans


print(productExceptSelf([-1,1,0,-3,3]))