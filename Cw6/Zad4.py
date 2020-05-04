import numpy as np


def generuj(potega, ilosc):
    return np.logspace(1, ilosc, num=ilosc, base=potega)


print(generuj(2, 4))
print(generuj(3, 3))