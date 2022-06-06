def numIdenticalPairs(nums):

    storetonums={}
    total=0
    count=0

    for x in nums:
        if x not in storetonums.values() :
            storetonums[count]=x
            count+=1
        else:
            for y in storetonums.values():
                if y==x:
                    total += 1
            storetonums[count] = x
            count += 1


    return total







print(numIdenticalPairs([1,1,1,1]))