import pandas as pd
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik)

temp = df[(df["Rok"] >= 2000) & (df["Rok"] <= 2005)]
suma = temp["Liczba"].sum()

print(suma)
