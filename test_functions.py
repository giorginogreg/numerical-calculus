from numpy import *


def f(x, derivative_order=0):
    if derivative_order == 1:
        return 1 + sin(x)
    return x - cos(x)


def g(x, derivative_order=0):
    if derivative_order == 1:
        return 1 + exp(-x)
    return x - exp(-x)
