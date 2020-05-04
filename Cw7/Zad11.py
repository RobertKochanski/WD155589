import numpy as np

a = np.arange(12).reshape(3, 4)
b = np.arange(12).reshape(4, 3)
c = np.arange(12).reshape(2, 6)
print(a)
print(b)
print(c)
print(f"a = {a.ravel()}")
print(f"b = {b.ravel()}")
print(f"c = {c.ravel()}")

