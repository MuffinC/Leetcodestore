def removeDuplicates(nums):
    counterdup=0
    originalval =len(nums)
    stack=[]
    popminus=0
    for x in range(0,len(nums),1):
        if x == len(nums)-1:
            break;
        if nums[x] == nums[x+1]:
            counterdup+=1
            stack.append(x)

    for y in stack:
        nums.pop(y+popminus) #in case you want the original array
        popminus -=1

    res = originalval-counterdup
    return res









x=[0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(x))