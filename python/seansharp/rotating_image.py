def rotate(matrix):
    import math

    y=-1
    # reverse the rows
    for x in range(math.floor(len(matrix)/2)):
        hold = matrix[x]
        matrix[x] = matrix[y]
        matrix[y] = hold
        y-=1

    #now to transpose the matrix... apperently leetcode doesnt allow np
    """
    import numpy as np
    matrix = np.array(matrix)
    matrix = matrix.transpose()
    matrix = matrix.tolist()
    """
    for x in range(len(matrix)):
        for y in range(x,len(matrix[0])):
            hold = matrix[x][y]
            matrix[x][y] = matrix[y][x]
            matrix[y][x] = hold

    return matrix

print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))