import math



def my_finitefunction(x):
    if(x == float('nan') or type(x) == float('inf')):
        return math.isfinite(x)
    if x == str:
        raise TypeError("Input cannot be string")   
    if not x:
        raise TypeError("Input cannot be empty")   
    return math.isfinite(x)