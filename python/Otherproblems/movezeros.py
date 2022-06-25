def moveZeroes(nums):
    x=0
    zerocount=0
    if len(nums)<2: return nums
    while x<len(nums):
        if nums[x]==0:
            zerocount+=1
            nums.pop(x)
        else:
            x+=1
    for x in range(zerocount):
        nums.append(0)
    return nums


print(moveZeroes([0,1,0,3,12]))