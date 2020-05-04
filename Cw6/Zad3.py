import numpy as np


def foo(x):
    return np.arange(1, x*x+1).reshape(x, x)


print(foo(5))
