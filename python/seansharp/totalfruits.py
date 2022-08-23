def totalFruit(fruits):
    """
    :type fruits: List[int]
    :rtype: int
    """
    if len(fruits) < 3: return len(fruits)
    res = []
    ans = float("-inf")


    for y in range(0, len(fruits)):
        if fruits[y] not in res and len(set(res))<2:
            res.append(fruits[y])
            ans = max(ans, len(res))
        elif fruits[y] not in res:
            g="*"
            ind=0
            for x in range(len(res)-1,-1,-1):
                if g=="*":
                    g=res[x]
                else:
                    if res[x] !=g:
                        ind=x+1
                        break
            res=res[ind:]
            res.append(fruits[y])
            ans = max(ans, len(res))

        else:
            res.append(fruits[y])
            ans=max(ans,len(res))



    return ans


print(totalFruit([3,3,3,1,4]))