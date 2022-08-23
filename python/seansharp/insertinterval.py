def insert( intervals, newInterval):
    """
    :type intervals: List[List[int]]
    :type newInterval: List[int]
    :rtype: List[List[int]]
    """
    intervals = intervals + [newInterval]
    intervals = sorted(intervals, key=lambda x: x[0])
    oldstart, oldend = intervals[0][0], intervals[0][1]
    res = []

    for newstart, newend in intervals:
        if newstart > oldend :
            res.append([oldstart,oldend])
            oldstart, oldend=newstart,newend
        elif newstart <= oldend and newstart>=oldstart and newend>=oldend:
            oldend=newend
    res.append([oldstart,oldend])



    return res


print(insert([[1,2],[3,5],[6,7],[8,10],[12,16]],[4,8]))