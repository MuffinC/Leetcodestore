def fib(n):
    """
    alpha =0
    beta =1
    if n==0:
        return alpha
    elif n==1:
        return beta
    else:
        for x in range(1,n,1):
            prev=beta
            beta=alpha +beta
            alpha=prev
        return beta
    """

    table=[0]*(n+1)
    table[1]=1
    #create a table of size n+1 with all zeros in them

    for x in range(0,n,1):
        table[x+1]+= table[x]
        if x==n-1: break
        table[x+2]+= table[x]

    return table[n]



print(fib(5))