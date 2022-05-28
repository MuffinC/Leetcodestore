def majorityElement(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

    
    if len(nums)<2:return nums[0]
    major=len(nums)/2
    set=[]
    count =[]
    for x in range(len(nums)):
        if nums[x] not in set:
            set.append(nums[x])
            count.append(1)
        else:
            for y in range(len(set)):
                if nums[x]== set[y]:
                    count[y]=count[y]+1
                if count[y]>major:
                    return set[y]
"""
    nums.sort()
    lenb = len(nums)
    return nums[int(lenb / 2)]

"""


print(majorityElement([3,2,3]))