import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

plik = pd.ExcelFile("imiona.xlsx")
df = pd.read_excel(plik)

lata = df[((df["Rok"] <= 2017) & (df["Rok"] > 2012))]
grupa = lata.groupby(["Plec"]).agg({"Liczba":["sum"]})

wykres = grupa.plot.pie(subplots=True, autopct="%.2f %%", fontsize=20, figsize=(6, 6))
plt.show()

