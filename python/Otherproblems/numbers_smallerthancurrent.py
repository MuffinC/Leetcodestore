def smallerNumbersThanCurrent(nums):
    dct = {}
    for i, n in enumerate(sorted(nums)):
        #i=count, n = element
        if n not in dct:
            dct[n] = i
    return [dct[n] for n in nums]

print(smallerNumbersThanCurrent([8,1,2,2,3]))