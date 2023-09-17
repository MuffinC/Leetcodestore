def merge(intervals):

    if len(intervals) == 1: return intervals
    intervals = sorted(intervals)
    l = 1
    curstart, curend = intervals[0][0], intervals[0][1]
    ans = []
    # sort by the start
    while l < len(intervals):
        if intervals[l][0] < curend:
            # able to merge
            curend = intervals[l][1]
        else:
            if curstart != intervals[l][0] and curend != intervals[l][1]:
                ans.append([curstart, curend])
            curstart = intervals[l][0]
            curend = intervals[l][1]
            ans.append([curstart, curend])
        l += 1

    return ans
print(merge([[1,3],[2,6],[8,10],[15,18]]))