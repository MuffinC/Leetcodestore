def climbStairs(n):
    alpha=1
    beta=1
    for x in range(1,n,1):
        hold=beta
        beta = alpha+beta
        alpha = hold
    return beta







print(climbStairs(4))