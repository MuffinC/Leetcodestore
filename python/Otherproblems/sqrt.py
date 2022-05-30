def mySqrt(x):
    """
    :type x: int
    :rtype: int
    """
    if x == 2:
        return 1
    if x>1:
        for y in range(2,x,1):
            if y*y == x:
                return y
            else:
                truncn = int(x/y)
                if(truncn*truncn < x ):
                    return int(x/y)
    else:
        return x

def mysqert2(x):
    y = 0
    z = 0
    sqr = 0
    while(sqr<=x):
        if(sqr == x):
            return z
        else:
            y = z
            z = z+1
            sqr = z*z
    return y



print(mysqert2(100))