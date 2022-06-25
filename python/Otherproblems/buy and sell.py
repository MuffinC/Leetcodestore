def zigzagLevelOrder(root):
    total=0
    for x in range(len(root)):
        if(x==0):
            buy=root[x]
            sell=root[x]
        if (root[x] > buy) and (root[x] > sell):
            sell = root[x]
        if(root[x]<sell) or x==len(root)-1:
            #cashout
            total+=sell-buy
            buy = root[x]
            sell = root[x]



    return total










print( zigzagLevelOrder([7,6,4,3,1]))