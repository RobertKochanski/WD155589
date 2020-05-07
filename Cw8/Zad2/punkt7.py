import pandas as pd
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik)


suma = df.groupby(["Imie"])["Liczba"].sum()
print(suma.max())