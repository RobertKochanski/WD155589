import pandas as pd
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik)

M = df[(df["Plec"] == "M")]
K = df[(df["Plec"] == "K")]
SM = M["Liczba"].sum()
SK = K["Liczba"].sum()

print(SM)
print(SK)
