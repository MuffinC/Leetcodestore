import math


def searchMatrix( matrix, target):

    Lrow=len(matrix)-1
    cols=len(matrix[0])-1
    for row in range(len(matrix)):
        if target<matrix[row][0]:
            Lrow=row-1
            break
    # run bfs in the row that the target is suspected to be in


    l=0
    r=cols
    if l==0 and r==0 and matrix[Lrow][0]== target: return True
    if l!=r:
        while r-l!=1:
            mid=math.floor((l+r)/2)
            if matrix[Lrow][mid]>= target:
                r=mid
            elif matrix[Lrow][mid]< target:
                l=mid
        if matrix[Lrow][l] == target or matrix[Lrow][r]==target: return True
    return False






print(searchMatrix([[1],[3]],13))