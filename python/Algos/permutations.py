def permutate(nums):
    res = []
    #solve base case
    if len(nums) == 1 : return [nums[:]]
    for x in range(len(nums)):
        y = nums.pop(0)
        perms = permutate(nums) #in leet code it is self.permute for recurssion

        for perm in perms: perm.append(y)
        res.extend(perms)
        nums.append(y)
    return res






print(permutate([1,2,3]))