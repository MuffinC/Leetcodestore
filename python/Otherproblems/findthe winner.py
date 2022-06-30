def findTheWinner(n, k):
    """
    :type n: int
    :type k: int
    :rtype: int
    """
    circle = [x for x in range(1,n+1)]
    point=0

    def progress(point, circle,k):
        if len(circle) ==1: return circle[0]
        res=point+(k-1)
        while res>=len(circle):
            res=res-len(circle)
        circle.pop(res)

        return progress(res,circle,k)

    return progress(point, circle, k)





print(findTheWinner(6,5))