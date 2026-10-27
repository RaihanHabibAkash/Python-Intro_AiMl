# https://www.deep-ml.com/problems/1
# Write a Python function that computes the dot product of a matrix and a vector. The function should return a list representing the resulting vector if the operation is valid, or -1 if the matrix and vector dimensions are incompatible. A matrix (a list of lists) can be dotted with a vector (a list) only if the number of columns in the matrix equals the length of the vector. For example, an n x m matrix requires a vector of length m.

# Example:
# Input:
# a = [[1, 2], [2, 4]], b = [1, 2]
# Output:
# [5, 10]
# Reasoning:
# Row 1: (1 * 1) + (2 * 2) = 1 + 4 = 5; Row 2: (2 * 1) + (4 * 2) = 2 + 8 = 10

import numpy as np

def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
	mat = np.array(a)
	v = np.array(b)

	mat_shape = mat.shape

	if mat_shape[1] != v.size :
		return -1
 
	return np.dot(mat, v).tolist()