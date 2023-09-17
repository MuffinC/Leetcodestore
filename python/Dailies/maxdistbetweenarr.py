def maxDistance(arrays):
    # sort arrays by [min max] then pop the min and then sort again to get the max
    holder = []
    for arr in arrays:
        holder.append([min(arr), max(arr)])
    second=holder.copy()
    holder = sorted(holder, reverse=True, key=lambda x: x[1])
    shadows, maxi = holder.pop(0)
    holder = sorted(holder)
    mini, shadowb = holder.pop(0)
    ans1=max(abs(shadowb - shadows), abs(maxi - mini))

    #second
    second = sorted(second)
    Smini, Sshadowb = second.pop(0)
    second = sorted(second, reverse=True, key=lambda x: x[1])
    Sshadows, Smaxi = second.pop(0)
    ans2=max(abs(Sshadowb - Sshadows), abs(Smaxi - Smini))

    return max(ans1,ans2)
print(maxDistance([[-6,-3,-1,1,2,2,2],[-10,-8,-6,-2,4],[-2],[-8,-4,-3,-3,-2,-1,1,2,3],[-8,-6,-5,-4,-2,-2,2,4]]))