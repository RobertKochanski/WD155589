import numpy as np

a = np.arange(9).reshape(3, 3)
print(a)
for x in a.flat:
    print(x)