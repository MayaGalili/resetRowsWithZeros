"""
Script Goal:
Given a NXN binary matrix, produce a new matrix in 
which all rows and columns are zeroed if one of their
cells in the original matrix contains zero. In the most efficient way (time and space).

Created on Tue May 22 15:03:36 2018
@author: Maya Galili
"""

import numpy as np


def reset_rows_with_zeros(input_matrix):
    mat_sz = len(input_matrix)
    v1 = np.sum(input_matrix, axis=1)
    v2 = np.sum(input_matrix, axis=0)

    # zero out rows and columns containing zeros
    for i in range(0, mat_sz):
        if v1[i] < mat_sz:
            input_matrix[i, :] = 0
        if v2[i] < mat_sz:
            input_matrix[:, i] = 0

    print('RESULTS', input_matrix)
    return input_matrix
