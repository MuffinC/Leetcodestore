def findIndices(nums, indexDifference, valueDifference):
    # [(value, index),... ,()]
    if len(nums) <= indexDifference: return [-1, -1]
    if len(nums) < 2:
        if nums and indexDifference == 0 and valueDifference == 0:
            return [0, 0]
        else:
            return [-1, -1]
    table = []
    for x in range(len(nums)):
        table.append((nums[x], x))
    table = sorted(table)

    if abs(table[-1][0] - table[0][0]) < valueDifference: return [-1, -1]

    for x in range(len(table) - 1):
        if abs(table[x][0] - table[-1][0]) >= valueDifference:
            if abs(table[x][1] - table[-1][1]) >= indexDifference:
                return [table[x][1], table[-1][1]]
        else:
            break

    for x in range(len(table)-1,-1,-1):
        if abs(table[x][0] - table[0][0]) >= valueDifference:
            if abs(table[x][1] - table[0][1]) >= indexDifference:
                return [table[x][1], table[0][1]]
        else:
            break

    for y in range(len(table) - 1, -1, -1):
        if abs(y - 0) >= indexDifference:
            if abs(nums[y] - nums[0]) >= valueDifference:
                return [y, 0]
        else:
            break

    return [-1, -1]


print(findIndices([6,23,41,44,11,18,38,14,4,26,8,44,27,36,41,18,43,2,12,26,38,38,49,33,36,15,9,22,45,27,32,10,24,24,48,29,15,41],18,44))
