def findDuplicates(nums):
    store = {}
    #item: index
    ans = []
    #Hash map its always index , value for enumerate but we store it as value: index
    for x,y in enumerate(nums):
        if y in store:
            ans.append(y)
        store[y] = x# value = index
    return ans

print(findDuplicates([4,3,2,7,8,2,3,1]))