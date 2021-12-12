from numpy import *


def LU_factorization(M):
    """ Function that compute Lower-Upper Factoriation of the input matrix

    If this file is executed standalone, it will output an example of the factorization


    Input:
    ------
        M: matrix
            Input Matrix to which calculate factorization

    Output:
    -------
        [L,U]: List
            L: Lower special triangular matrix
            U: Upper triangular matrix

    """
    [n, n] = shape(M)

    An = copy(M)  # An = L * A
    L = identity(n)  # Index goes through [1, n], [0,n-1]

    for j in range(0, n-1):  # Columns
        for i in range(j+1, n):  # Rows
            multiplier = - An[i, j] / An[j, j]
            for k in range(j+1, n):
                An[i, k] += multiplier*An[j, k]
            L[i, j] = -multiplier

    U = triu(An)
    return (L, U)


[L, U] = LU_factorization(matrix([
    [2, 1, 0, - 1],
    [-2, -2, 1, - 1],
    [4, 2, - 1, - 1],
    [0, 2, -3, 2]
])
)
print("Lower Matrix:")
print(L)
print("Upper Matrix:")
print(U)
