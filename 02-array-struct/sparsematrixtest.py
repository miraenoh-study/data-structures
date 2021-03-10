from SparseMatrix import *

# Create a new sparse matrix
print('Create a new sparse matrix')
sample_matrix = SparseMatrix(6, 6, 8, [Term(0, 0, 15), Term(0, 3, 22), Term(
    0, 5, -15), Term(1, 1, 11), Term(1, 2, 3), Term(2, 3, -6), Term(4, 0, 91), Term(5, 2, 28)])
sample_matrix.print()

# Transpose the sample matrix
print('\nTranspose the matrix')
transposed_matrix = sample_matrix.transpose()
transposed_matrix.print()

# Transpose again with the fast_transpose method
print('\nTranspose again with the fast_transpose method')
fast_transposed_matrix = sample_matrix.fast_transpose()
fast_transposed_matrix.print()

# Test the matrix multiplication
print('\nMatrix multiplication')
matrix_a = SparseMatrix(3, 3, 3, [Term(0, 0, 1), Term(1, 0, 2), Term(2, 0, 3)])
matrix_b = SparseMatrix(3, 3, 3, [Term(0, 0, 1), Term(0, 1, 2), Term(0, 2, 3)])
print('Matrix A')
matrix_a.print()
print('Matrix B')
matrix_b.print()
matrix_result = SparseMatrix.mmult(matrix_a, matrix_b)
print('Result of mmult')
matrix_result.print()

# Test the matrix addition
print('\nMatrix addition')
matrix_a = SparseMatrix(3, 3, 3, [Term(0, 1, 3), Term(1, 0, 2), Term(2, 0, 3)])
matrix_b = SparseMatrix(3, 3, 3, [Term(0, 0, 1), Term(0, 1, 2), Term(0, 2, 3)])
print('Matrix A')
matrix_a.print()
print('Matrix B')
matrix_b.print()
matrix_result = SparseMatrix.madd(matrix_a, matrix_b)
print('Result of madd')
matrix_result.print()