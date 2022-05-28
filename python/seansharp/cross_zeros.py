def setZeroes(matrix):
    """
    :type matrix: List[List[int]]
    :rtype: None Do not return anything, modify matrix in-place instead.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    for x in range(rows):
        #x = rows
        #y = cols
        for y in range(cols):
            if matrix[x][y] ==0:
                for a in range(cols):
                    if matrix[x][a] != 0:
                        matrix[x][a] = 'a'
                for b in range(rows):
                    if matrix[b][y] != 0:
                        matrix[b][y] = 'a'
    for x in range(rows):
        for y in range(cols):
            if matrix[x][y] =='a':
                matrix[x][y] =0

    return matrix

print(setZeroes([[0,1]]))