def searchMatrix(matrix, target):
    """
    :type matrix: List[List[int]]
    :type target: int
    :rtype: bool
    """
    row = len(matrix)
    col = len(matrix[0])
    Lans = '*'
    for x in range(0, row):
        if target <= matrix[x][-1]:
            Lans = x
            break
    if Lans == '*': return False

    for y in range(0, len(matrix[Lans])):
        if target == matrix[Lans][y]:
            return True
    return False

print(searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))
