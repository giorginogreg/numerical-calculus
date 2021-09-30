def newton(f, x0, tol=1e-10, maximum_iterations=100):
    """
    Newton method
    ------------------------
    Syntax:
        alpha = newton(f, x0, tolerance, maximum_iterations)

        f: function to which calculate alpha value
        x0: initial estimation of the zero function
        tolerance: maximum value of tolerance, required precision
        maximum_iterations: the number of maximum iterations that you want to do

    Output data:
        x1: zero approximation of f(x)
        executed_iterations: no. of iterations that the algorithm has been executed

    """

    have_to_stop = False
    iterator = 0
    while not(have_to_stop) and iterator < maximum_iterations:
        iterator = iterator + 1
        x1 = x0-f(x0)/f(x0, 1)
        print("x1 value: " + str(x1))
        have_to_stop = abs(x1 - x0) < tol  # Estimation of absolute error
        x0 = x1
    if not(have_to_stop):
        print("Precision not reached")
    return x1, iterator
