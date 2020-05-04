import numpy as np

a = np.array([2, 3, 4])
b = np.array([5, 6, 7])

print(a.dot(b))
# //////// INNY SPOSÓB /////////////
print(np.dot(a, b))
