def findMinArrowShots(points):
    points = sorted(points, key=lambda x: x[1]) #sorts it based on the second value
    res, end = 0, -float('inf')
    for interval in points:
        if interval[0] > end:
            res += 1
            end = interval[1]
    return res

print(findMinArrowShots([[10,16],[2,8],[1,6],[7,12]]))