import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik)

grupa = df.groupby(['Plec']).agg({'Liczba':['sum']})
print(grupa)

wykres = grupa.plot.bar()
wykres.set_ylabel('Liczba')
wykres.set_xlabel('Płeć')
wykres.legend()
wykres.plot()
plt.show()

