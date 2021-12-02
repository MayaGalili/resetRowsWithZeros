# -*- coding: utf-8 -*-
"""
Script Goal:
Given a NXN binary matrix, produce a new matrix in 
which all rows and columns are zeroed if one of their
cells in the original matrix contains zero.

Created on Tue May 22 15:03:36 2018
@author: Maya Galili
"""

import numpy as np

def main(mat_size):
    # create random binary matrix
    v1=np.zeros(mat_size)
    v2=np.zeros(mat_size)
    M=np.random.randint(2,size=(mat_size,mat_size))

    print('TEST MATRIX')
    print(M)

    v1 = np.sum(M,axis=1)
    v2 = np.sum(M,axis=0)    

    print('V1')
    print(v1)
    print('V2')
    print(v2)

    # zero out rows and columns containig zeros
    for i in range(0,mat_size):
        if (v1[i] < mat_size):
            M[i,:] = 0
        if (v2[i] < mat_size):
            M[:,i] = 0    

    print('RESULTS')
    print(M)

if __main__ == "__name__":
    MAT_SZ = 25
    main(MAT_SZ)   
