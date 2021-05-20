import numpy


def create_matrix(m, n):
    matrix = [([0]*n) for i in range(m)]
    print(matrix)
    return matrix


def create_matrix_numpy(m, n):
    matrix = numpy.zeros((m, n))
    print(matrix)
    return matrix


def matrix_index(m, n, matrix):
    print(matrix[m][n])


def matrix_index_numpy(m, n, matrix):
    print(matrix[m, n])


if __name__ == '__main__':

    matrix_ = create_matrix(3, 4)
    matrix_numpy = create_matrix_numpy(3, 5)
    matrix_index(1, 1, matrix_)
    matrix_index_numpy(1, 1, matrix_numpy)

    print("Input array length:")
