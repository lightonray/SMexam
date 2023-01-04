import math


def my_finitefunction(x):
    if (type(x) == math.isnan(x) or type(x) == math.isinf(x)):
        return math.isfinite(x)
    if x == str:
        raise TypeError("Input cannot be string")
    if not x:
        raise TypeError("Input cannot be empty")
    return math.isfinite(x)
