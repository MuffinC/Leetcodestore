def maxProfit(prices):
    minpt =prices[0]
    maxpt =prices[0]
    max =0
    for x in range(1,len(prices)):
        if prices[x]<minpt:
            minpt = prices[x]
            maxpt = prices[x]
        elif prices[x]>maxpt:
            maxpt = prices[x]
        if maxpt-minpt>max:
            max = maxpt-minpt
    return max






print(maxProfit([7,1,5,3,6,4]))