def missingNumber(nums):
    """
        for x in range(len(nums)+1):
        if x not in nums:
            return x
    """
    #alternatively
    return sum(range(len(nums)+1))-sum(nums)

print(missingNumber([9,6,4,2,3,5,7,0,1]))