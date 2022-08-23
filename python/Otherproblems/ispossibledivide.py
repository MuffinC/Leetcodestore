def isPossibleDivide(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k > len(nums) or len(nums) % k != 0: return False

    # create a hash map of val: count
    table={}
    nums=sorted(nums)
    for x in nums:
        if x not in table:
            table[x]=1
        else: table[x]+=1
    #table => val:count
    while sum(table.values())!=0:
        cur=0


    return True

print(isPossibleDivide([16,21,26,35],4))