def cust(N,K,W,orders):
    res=[]
    real=0 #starting curr time
    old=0
    backlog=[]
    for y in range(len(orders)):
        if (orders[y][0] + orders[y][1]) > orders[y+1][0]:
            backlog.append(orders[y+1])

    backlog =sorted(orders, key=lambda x:x[1])




    for x in orders:
        start,duration=x
        if real<= start:
            #when there is no delay
            profit=duration*K
            real=start+duration
        else:

            profit = (duration * K)-((real-start)*W)
            real=duration
        res.append(profit)
    return res





print(cust(3,5,1,[[1,4],[2,2],[9,1]]))

#5,10,1,[[3,5],[4,2],[4,1],[10,15],[15,2]