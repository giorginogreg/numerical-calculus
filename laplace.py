"""Computation of matrix determinant using Laplace algorithm

"""
from numpy import *


def laplace(M):
    """
    Input param
    -----------
        M: Matrix
            Matrix for determinant computation

    Output param
    ------------
        determinant: float
            Value of the matrix determinant
    """
    [m, n] = shape(M)
    if n == 1:
        determinant = M[0, 0]
    else:
        determinant = 0
        for j in range(0, n):
            Msub1j = delete(M, 0, axis=0)
            Msub1j = delete(Msub1j, 0, axis=1)
            determinant += (-1) ** j * M[0, j] * laplace(Msub1j)
    return determinant
