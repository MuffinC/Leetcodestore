def open_or_senior(data):
    res=[]
    ans=["Open","Senior"]

    #age:handi
    for x in data:
        y=0
        if x[y]>=55:
            if x[y+1]>7:
                res.append(ans[1])
            else:
                res.append(ans[0])
        else:
            res.append(ans[0])
    return res

print(open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)]))