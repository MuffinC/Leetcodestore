def isPowerOfThree(n):
    if n==1: return True
    if n<3: return False
    x=3
    while (x<n):
        if n %x!=0:
            return False
        x=x*3
        if n %x!=0:
            return False
    return True

print(isPowerOfThree(6))