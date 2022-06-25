def cansum(candidates, target,memo={},lister=[]):

    if target in memo: return memo[target]
    if target==0: return True
    if target<0: return False

    for x in candidates:
        rem=target-x
        if(cansum(candidates,rem,memo)):
            memo[target]=True
            return True
        #just take the boolean result and assign to the target
    memo[target]=False
    return False








print(cansum([2,3,6,7],7))