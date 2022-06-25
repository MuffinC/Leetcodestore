def longestConsecutive(nums):
    if len(nums)<1: return 0

    hold=set(nums)
    total=0
    l=1
    res=1
    for x in hold:
       if x -1 not in hold:
            #start of sequence found
            while x+l in hold:
                res+=1
                l+=1
            total=max(total,res)
            res=1
            l=1
       else: continue

    return total



print(longestConsecutive([1,-8,7,-2,-4,-4,6,3,-4,0,-7,-1,5,1,-9,-3]))