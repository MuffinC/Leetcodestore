def eraseOverlapIntervals(intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    intervals=sorted(intervals,key= lambda x: x[1])
    cnt,end=0,float("-inf")
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            cnt += 1
    return cnt
print(eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))

