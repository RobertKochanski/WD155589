import numpy as np

a = np.arange(81).reshape(9, 9) # macierz 9x9
print(a)
print(a.shape)
b = a.reshape((3,27)) # macierz 3x27
print(b)
print(b.shape)
c = a.ravel() # macierz spłaszczona
print(c)
print(c.shape)
d = a.T # transpozycja macierzy a
print(d)
print(d.shape)
