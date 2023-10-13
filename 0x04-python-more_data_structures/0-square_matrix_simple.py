#!/usr/bin/python3
def square_matrix_simple(matrix):
    """gives a matrix with its elements squared

    Args:
        matrix (list): the matrix

    Returns:
        list: matrix
    """
    
    new_mat = matrix.copy();

    for i in range(len(matrix)):
        new_mat[i] = list(map(lambda x: x**2, matrix[i]))
    return (new_mat)


