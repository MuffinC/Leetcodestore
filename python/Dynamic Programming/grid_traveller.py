def gridtraveller(m,n,memo={}):


    if (m,n) in memo: return memo[(m,n)]

    if m==1 and n ==1: return 1
    if m==0 or n==0: return 0
    # so u are basically pasing the same memo into all the recurssive calls
    memo[(m,n)]=gridtraveller(m-1,n,memo)+gridtraveller(m,n-1,memo)
    return memo[(m,n)]
    #memo is not needed in the outer because it is automaticallly created in the 1st function call


"""
    #tabulation
    tabler=[[0]*(n+1)]*(m+1)
    tabler[1][1]=1 #this somehow doesnt fill...
    for x in range(0,m,1):
        for y in range(0,n,1):
            cur=tabler[x][y]
            if(y+1<=n): tabler[x][y+1]=+cur
            if(x+1<=m): tabler[x+1][y]=+cur
    return tabler
"""







print(gridtraveller(3,2))