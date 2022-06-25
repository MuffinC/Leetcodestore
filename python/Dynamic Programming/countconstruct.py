def countconstruct(target,words,memo={}):
    if target == '': return 1
    if target in memo: return memo[target]
    total=0

    for x in words:
        if target.startswith(x):
            suffix=target[len(x):]
            nums=countconstruct(suffix,words,memo)
            total+=nums

    memo[target]=total
    return total




print(countconstruct('purple',['purp','p','ur','le','purpl']))