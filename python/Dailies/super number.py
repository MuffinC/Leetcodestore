def superDigit(n, k):
    # Write your code here
    ans=0
    for x in list(n):
        ans = ans + (int(x) * k)
    n = str(ans)

    while int(n)>9:
        ans=0
        for y in list(n):
            ans +=int(y)
        n = str(ans)
        ans=0
    return n

print(superDigit('148',3))