import numpy as np


a = np.sin(np.arange(6).reshape(2, 3))
b = np.cos(np.arange(6).reshape(2, 3))

print(a)
print(b)
print(np.add(a, b))
