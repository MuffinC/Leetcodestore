def combinationSum2(candidates, target):
    table = {}
    for x in candidates:
        if x not in table and x <= target:
            table[x] = 1
        else:
            table[x] += 1
    return

print(combinationSum2([10,1,2,7,6,1,5], 8))