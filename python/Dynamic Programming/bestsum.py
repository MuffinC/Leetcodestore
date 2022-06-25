def bestsum(target, numbers,memo={}):
    #you want to return only the shortest array
    if target in memo: return memo[target]
    if target ==0: return []
    if target<0: return None

    shortest=None

    for x in numbers:
        ret=target-x
        remcombi=bestsum(ret,numbers,memo)

        if remcombi!=None:
            memo[target]=remcombi.copy()+[x]

            if (shortest==None) or (len(memo[target])<len(shortest)):
                shortest=memo[target]


    return shortest



#print(bestsum(7,[5,3,4,7]))
#print(bestsum(8,[2,3,5]))

print(bestsum(100,[2,1,4,25]))

