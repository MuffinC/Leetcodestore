def twoSum(nums, target):
    difftoind={}
    for x,y in enumerate(nums):
        difftoind[target-y]=x
    count=0
    for x in nums:
        if x in difftoind and (count!=difftoind[x]):
            return [count,difftoind[x]]
        count+=1




print(twoSum([3,2,4],6))