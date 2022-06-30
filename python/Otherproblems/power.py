def myPow(x, n):
    # x^n
    res=1
    if n==0: return res

    def power(res,x,n):
        if n==0: return res
        if n<0:
            return power(res*x,x,n+1)
        if n>0:
            return power(res*x,x,n-1)

    if n>0: return power(res,x,n)
    if n<0: return 1/(power(res,x,n))










print(myPow(2.0000,-2))