class MatrixContentError(Exception):
    pass

class MatrixSizeError(Exception):
    pass

def rotate_matrix(matrix):
    matrix_length = len(matrix)

    for i in range(matrix_length):
        for j in range(i, matrix_length):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(matrix_length):
        matrix[i].reverse()

mtrx = []

while True:
    line = input().split()
    for ch in line:
        if not ch.isdigit():
            raise MatrixContentError("The matrix must consist of only integers")

    if not line:
        break
    mtrx.append(line)

if len(mtrx[0]) != len(mtrx):
    raise MatrixSizeError("The size of the matrix is not a perfect square")

rotate_matrix(mtrx)

for row in mtrx:
    print(*row, sep=' ')
