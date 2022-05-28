def spiralOrder(matrix):
    return matrix and [*matrix.pop(0)] + spiralOrder([*zip(*matrix)][::-1])



print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))