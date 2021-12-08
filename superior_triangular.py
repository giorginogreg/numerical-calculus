from numpy import *


def superior_triangular(M, b):
    """Function that computes an array of not known values deriving from a matrix to give in input.

    Need to considerate that matrix determinant (obtained thanks to the product of the principal diagonal) is not equal to 0:
    i.e. each element in the principal diagonal is not equal to zero

    Input values
    ------------
        M: matrix
            Matrix to which compute unknown values - Needs to be a upper triangular matrix
        b: array
            List of known values

    Output values
    -------------
        x: array
            List of array solutions of Ax = b system
            It will have a n dimension

    How to use this function:
    -------------------------
        - b = random.rand(n, 1)
        - M = triu(random.rand(n,n))
        - x = superior_triangular(M, b)
        if dot(M, x) - b  produces an array of zeroes, the algorithm is correct
    """
    [rows, cols] = shape(M)
    x = zeros(shape=(cols, 1))  # Allocating memory for array x
    tol = 1e-15
    # Iterate through each row of M from n to 0 (in machine algebra)
    for i in range(cols - 1, -1, -1):
        if abs(M[i, i]) < tol:  # Evaluate if each elem of principal diagonal is not equal to 0
            print("Error: Singular matrix - determinant equal to 0")
            return nan
        else:
            sum = 0
            for j in range(i+1, cols):
                sum += M[i, j] * x[j]
            x[i] = (b[i] - sum) / M[i, i]
    return x
