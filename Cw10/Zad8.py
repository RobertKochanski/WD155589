import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as r


def rzucaj(n):
    wynik = []
    for i in range(n):
        x = r.randint(1, 6)
        y = r.randint(1, 6)
        wynik.append(x + y)
    print(wynik)
    plt.hist(wynik, bins=12, facecolor='g', alpha=0.75, density=True)
    plt.xlabel('Wartości')
    plt.ylabel('Prawdopodobieństwo')
    plt.title('Histogram')
    plt.grid(True)
    plt.show()


rzucaj(50)
