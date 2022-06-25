def construct2DArray(original, m, n):
    if len(original)!=(m*n): return []
    res =[[0]*n for k in range(m)]
    tot=0
    for x in range(m):
        for y in range(n):
            res[x][y]=original[tot]
            tot+=1
    return res



print(construct2DArray([1,2,3,4],2,2))