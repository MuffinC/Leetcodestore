def findDisappearedNumbers(nums):
    #is [1,n] and u want to find all missing values from the range
    """
    Time limit exceeded
    missing=[]
    for x in range(1,len(nums)+1):
        if x not in nums:
            missing.append(x)
    return missing
    """

    for i in range(len(nums)):
        temp = abs(nums[i]) - 1
        if nums[temp] > 0:
            nums[temp] *= -1

    res = []
    for i, n in enumerate(nums):
        if n > 0:
            res.append(i + 1)

    return res





print(findDisappearedNumbers([1,1]))