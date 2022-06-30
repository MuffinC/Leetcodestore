def topKFrequent(nums, k):
    table={}
    for x,y in enumerate(nums):
        if y not in table:
            table[y]=1
        else:
            table[y]+=1
    res=[]
    z=0
    max=0

    while z!=k:
        for ke,va in table.items():
            if (ke not in res) and (va>max):
                max=va
                kex=ke
        res.append(kex)
        z+=1
        max=0
    return res



print(topKFrequent([1],1))
