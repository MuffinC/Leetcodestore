def maxNumberOfAlloys(n, k, budget, composition, stock,cost) :
    # figure out optimal machine to use based on graphs and distance between the points and stock
    malist = []
    for ind, machine in enumerate(composition):
        madist = 0
        for x in range(len(stock)):
            madist += abs(machine[x] - stock[x])
        malist.append((madist, ind))
    malist = sorted(malist)
    # first machine is the most optimal

    optimal = composition[malist[0][1]]
    alloy = -1
    v = 0
    while v <= budget:
        for x in range(len(optimal)):
            if stock[x] - optimal[x] < 0:
                v += (cost[x] * (-1 * (stock[x] - optimal[x])))
                if stock[x]==0: continue
                stock[x] -= optimal[x]
            else:
                if stock[x] == 0: continue
                stock[x] -= optimal[x]
        alloy += 1
    return alloy

print(maxNumberOfAlloys(9,3,90,[[10,9,1,3,3,5,5,10,7],[2,6,4,9,9,1,9,6,7],[1,4,7,6,7,7,10,6,6]],[3,10,10,8,10,5,7,1,2],[9,8,10,9,9,3,9,5,8]))