

def productExceptSelf(nums):
    #prefix and suffix products
    import operator
    from itertools import accumulate
    prefix = list(accumulate(nums, operator.mul))
    suffix = list(accumulate(nums[::-1], operator.mul)) #this will get the right side from i
    res=[]
    for x in range(len(nums)):

        res.append((prefix[x-1] if x else 1) * (suffix[x+1] if x+1 < len(nums) else 1))
    return res



print(productExceptSelf([1,2,3,4]))