def canPartition(nums):
    if sum(nums) % 2 !=0: return False
    target=int(sum(nums)/ 2)
    subarray = set()
    subarray.add(0)
    for x in range(0,len(nums)):
        adder=set()
        for y in subarray:
            adder.add(y+nums[x])
            #adder.add(y)# adds the old subarray value back in
        subarray.update(adder)


    return True if target in subarray else False



print(canPartition([1,5,11,5]))