def canCompleteCircuit(gas, cost):
    #greedy?
    if sum(gas)<sum(cost): return -1

    total=0
    res=0

    for i in range(len(gas)):
        total+=gas[i]-cost[i]
        if total<0:
            total=0
            res=i+1
    return res


    #we now want to traverse the list to find the index that makes it possible







print(canCompleteCircuit([5,8,2,8],[6,5,6,6]))
