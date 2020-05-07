import pandas as pd
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik)

kopia = df.copy()
kopia["Max"] = df.groupby(["Rok", "Plec"])["Liczba"].transform(max)
wynik = kopia[kopia["Liczba"] == kopia["Max"]]
print(wynik)
