def howsum(candidates, target, memo={}):

    if target in memo: return memo[target]
    if target == 0: return []
    if target < 0: return None

    for x in candidates:
        rem = target - x
        resresult = howsum(candidates,rem,memo)
        if resresult != None:
            memo[target]= resresult[:] + [x]
            return memo[target]
    memo[target]=None
    return None


#print(howsum([2,3], 7))
print(howsum([2,3,6,7], 7))
#print(howsum([2, 4], 7))
#print(howsum([2,3,5], 8))
