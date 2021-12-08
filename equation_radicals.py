import numpy as np
def eq_radical(a, b, c):
    """
    This function compute radicals of a second grade equation only if delta is greater to zero
    """
    delta = b**2 - 4 * a * c;
    if delta <= 0:
        print("Error: delta value is NOT greater than zero")
        return
    else:
        radical = np.sqrt(b**2 - 4 * a * c)
        return [+ radical, - radical]

