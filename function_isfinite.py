"import module"
import math


def my_finitefunction(x):
    "function"
    if not x:
        raise TypeError("Input cannot be empty")
    elif type(x) == str:
        raise TypeError("Input cannot be string")
    elif (type(x) == math.isnan(x) or type(x) == math.isinf(x)):
        return math.isfinite(x)
    return math.isfinite(x)
