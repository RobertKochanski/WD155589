import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

plik = pd.read_csv('zamowienia.csv', sep=";")

grupa = plik.groupby(['Sprzedawca']).agg({'idZamowienia': ['count']})
print(plik)

wykres = grupa.plot.bar()
wykres.set_ylabel('Ilosc zamowien')
wykres.set_xlabel('Sprzedawca')
wykres.legend()
wykres.plot()
plt.show()

