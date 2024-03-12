def memo(arr,ex):
    inte=[]
    for x,y in zip(arr,ex):
        inte.append([x,y])

    inte=sorted(inte)
    start=min(arr)
    end=max(ex)
    table={x:0 for x in range(start, end+1)}

    for time in range(start,end+1):
        for x,y in inte:
            if time <=y and time>=x:
                table[time]+=1
    res=max(table.values())
    for time,count in table.items():
        if count==res: return time


print(memo([ 1, 2, 9, 5, 5 ], [4, 5, 12, 9, 12]))