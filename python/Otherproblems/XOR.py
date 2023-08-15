def ans(n,s):
    s=list(s)
    if s=='1': return "YES"
    if s != '1' and len(s)<=1 : return "NO"

    table ={'1':0,'0':0}
    for x in s:
        table[x]+=1
    swap=0
    while swap<=n:
        if table['1'] >table['0']:
            table['1']-=1
        elif table['0'] >table['1']:
            table['0']-=1
        if table['1'] == table['0']:
            return "YES"
        swap+=1
    return "NO"






print(ans(5,'110110'))