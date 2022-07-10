def isNStraightHand(hand, groupSize):
    if len(hand) % groupSize != 0:return False
    else:

        table={}
        for x in hand:
            if x not in table: table[x]=1
            else: table[x]+=1
        #hash map val||count
        while sum(table.values())!=0:

            for z in range(0,groupSize,1):




        return True



print(isNStraightHand([1,2,3,6,2,3,4,7,8],3))