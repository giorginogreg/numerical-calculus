from numpy import *;
from matrix import multipliers;
def gauss_elimination(M, b):
    """Compute an array of equations starting from a coefficients matrix and a vector of results"""
    [n,m] = shape(M);
    for i in range(1, n):
        multipliers = multipliers(M[i:,:])
        for cols in range(1,m):
            M[i][cols] += multipliers[i] * M[i][cols]
        

    return