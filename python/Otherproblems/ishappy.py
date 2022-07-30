def isHappy(n):
    ans = 0
    hist=[]
    round=0
    while (ans not in hist):
        if round>0:
            n = ans
            hist.append(ans)
        round+=1
        #convert n into a list

        n=[int(x) for x in list(str(n))]
        ans = 0
        for x in n:
            ans=ans+(x**2)
        if ans ==1: return True
    return False





print(isHappy(2))