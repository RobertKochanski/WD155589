import numpy as np


def foo(dlugosc):
    return np.diag(np.arange(dlugosc, 0, step=-1))


print(foo(5))
