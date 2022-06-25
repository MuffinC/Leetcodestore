def findDuplicate(nums):
    hasher={}
    for x,y in enumerate(nums):
        if y not in hasher:
            hasher[y]=1
        else:
            return y


print(findDuplicate([1,3,4,2,2]))