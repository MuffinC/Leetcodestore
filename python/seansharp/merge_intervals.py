def merge(intervals):
    if len(intervals)<2: return intervals
    total=len(intervals)
    x=0
    intervals=sorted(intervals) #sort the stack first
    while x< total:
        mini=0
        maxi=1
        if (x == len(intervals) - 1): break
        if(intervals[x+1][mini] >= intervals[x][mini]) and(intervals[x+1][mini] <= intervals[x][maxi]):
            nmin=min(intervals[x][mini],intervals[x+1][mini])
            nmax=max(intervals[x][maxi],intervals[x+1][maxi])
            intervals.pop(x)
            intervals.pop(x)
            intervals.insert(x,[nmin,nmax])
            x=0
        elif(intervals[x][mini]>=intervals[x+1][mini]) and (intervals[x][mini]<=intervals[x+1][maxi]):
            nmin=min(intervals[x][mini],intervals[x+1][mini])
            nmax=max(intervals[x][maxi],intervals[x+1][maxi])
            intervals.pop(x)
            intervals.pop(x)
            intervals.insert(x,[nmin,nmax])
            x=0
        else:
            x+=1
            if (x == len(intervals) - 1): break

    return intervals





print(merge([[2,3],[5,5],[2,2],[3,4],[3,4]]))