"""Matrix definition
In this module will be a short explanation on how to define matrices, and how to manage them in python
"""
from numpy import *

# A = math.random(2, 4)

# Defining a 2x3 matrix
A = matrix([
    [1, 2, 3],
    [4, 5, 6]
])

B = matrix([
    [5, 4],
    [10, 1],
    [9, 6]
])

print("Vettore A")
print(A)

print("Seconda riga del vettore A: ")
print(A[1, :])

print("elemento in riga 0 e colonna 0")
print(A[0, 0:1])
print("elemento in riga 0 e colonna 0 e 1")
print(A[0, 0:2])

print("3a colonna di A")
print(A[:, 2])

print("Trasposta di una matrice:")
print(A.T)

print("Dimensioni di A:")
print(shape(A))

# Matrix product is possible only if the internal dimensions are the same.
print("A * B: ")
print(A * B)  # Possible only if the two matrixes are defined via matrix() operator
# Resulting matrix will have external dimensions

# If the matrixes had been defined as array, i should have used to use dot() operator

# Function that generate an array with the numbers from the first to the last - 1 parameters
arange(1, 11) # Generate an array with ten numbers, starting from 1 to 10
