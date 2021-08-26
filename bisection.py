
from numpy import *
def bisection(f, a, b, tol):
    """
    Function that compute next bisections of a function in input, and return an approximation of the zero's input function
    
    Input parameters:
		  f: Any function
		  a: First value of an interval
		  b: Second value of an interval
		  tol: Tolerance value
    Output parameters:
		  alpha: zero's function approximation
      
	  """
    
    fa = f(a)
    fb = f(b)
    if(fa * fb > 0):
        print("Error! The function doesn't change sign at intervals extremes.")
        return
    stop_condition = False
    it = 0
    while not stop_condition:
        c = (a+b) / 2
        it += 1
        fc = f(c)
        if fc == 0:
            return c, it
        elif fa * fc < 0:
            b = c
        else:
            a = c
            fa = fc
        stop_condition = abs(b-a) < tol
    return c, it

def f(x):
    return sin(x)
