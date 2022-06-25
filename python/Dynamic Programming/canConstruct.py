def canConstruct(target,letters,memo={}):

    if target in memo:return memo[target]
    if target=='': return True

    for x in letters:
        if target.startswith(x):
            #suffix is the target post cutting
            suffix= target[len(x):]
            if canConstruct(suffix,letters,memo):
                memo[target]=True
                return True
    memo[target]=False
    return False





print(canConstruct('a',['b']))