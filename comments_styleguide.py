# -*- coding: utf-8 -*-
""" This is a short comment or one-line called comment

Before this string, i need to use a blank row, then i can insert the long description of what i need to comment.
I can for example comment a class, or maybe a function.

When creating a function, i can comment the parameters with the following syntax:

Parameters
----------
parameter_1: type_param
    this parameter is the first that the function will take as an input
"""


def test_function(param_1):
    """Function that literally does nothing except that it takes one parameter in input and returns the parameter added with itself

    This function return the double of the input parameter. 

    Parameters
    ----------
    param_1: int
        The first parameter

    Returns
    -------
    int
        Double of the parameter in input

    """

    return param_1 * 2
