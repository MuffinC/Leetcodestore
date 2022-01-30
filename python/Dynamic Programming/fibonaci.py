def fib(n):
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


print(fib(5))