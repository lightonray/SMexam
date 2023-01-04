import math


def my_finitefunction(x):
    if not isinstance(x, int or float):
        raise TypeError("Input is not a number")
    if not x:
        raise TypeError("Input cannot be empty")
    else:
        return math.isfinite(x)