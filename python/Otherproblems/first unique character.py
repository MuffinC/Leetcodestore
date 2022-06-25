def firstUniqChar(s):
    hash={}
    inst={}
    va=0
    for x in s:
        if x not in hash:
            hash[x]=1
            inst[x]=va
            va+=1
        else:
            hash[x]+=1
            va+=1
    for x,y in hash.items():
        if y==1:
            return inst[x]
    return -1




print(firstUniqChar("dddccdbba"))
