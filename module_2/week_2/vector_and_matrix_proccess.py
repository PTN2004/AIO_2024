import numpy as np


def compute_vector_lenght(vector):
    return np.sqrt(np.sum(vector * vector))


def compute_dot_product(vector_u, vector_v):
    dot_product = np.sum(vector_u * vector_v)
    return dot_product

def matrix_multi_vector(matrix, vector):
    row_matrix, column_matrix = matrix.shape
    row_vector = vector.shape[0]

    if column_matrix != row_vector:
        print(f"Matrix {matrix.shape} cannot be multiplied by vector {vector.shape}")
        return
    result = np.sum(matrix * vector, axis=0)
    
    return result

def matrix_multi_matrix(matrix1, matrix2):
    column_matrix1 = matrix1.shape[1]
    column_matrix2 = matrix2.shape[0]

    if column_matrix1 != column_matrix2:
        print(f"Matrix {matrix1.shape} cannot be multiplied by vector {matrix2.shape}")
        return
    
    result = np.dot(matrix1, matrix2)
    return result


def inverse_matrix(matrix):
    det_matrix = np.linalg.det(matrix)
    if det_matrix == 0:
        print("Matrix is not invertible!")
        return
    
    result = np.linalg.inv(matrix)
    return result

def compute_eigenvector_eigenvalue(matrix):
    eigenvalue, eigenvector = np.linalg.eig(matrix)
    return eigenvalue, eigenvector

def compute_cosine(v1, v2):
    result = np.dot(v1, v2) / (compute_vector_lenght(v1) * compute_vector_lenght(v2))
    return result


v1 = np.array([5, 3, 2, 7])
v2 = np.array([2, 9, 4, 1])

print(compute_cosine(v1, v2))