import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import xlrd
import openpyxl

plik = pd.ExcelFile('imiona.xlsx')
df = pd.read_excel(plik)

wykres1 = df.groupby("Plec")["Liczba"].sum().reset_index()
wykres3 = df.groupby(["Plec", "Rok"])["Liczba"].sum().reset_index()
wykresK = wykres3[wykres3["Plec"] == "K"].reset_index()
wykresM = wykres3[wykres3["Plec"] == "M"].reset_index()

plt.subplot(131)
plt.bar(wykres1["Plec"], wykres1["Liczba"], color=["b", "g"])
plt.xlabel("Plec")
plt.ylabel("Ilosc")

plt.subplot(132)
plt.bar(wykresK["Rok"], wykresK["Liczba"], color="b")
plt.bar(wykresM["Rok"], wykresM["Liczba"], color="r", bottom=wykresK["Liczba"])
plt.xlabel("Rok")
plt.ylabel("Ilosc")

plt.subplot(133)
plt.bar(wykres3["Rok"], wykres3["Liczba"], color="c")
plt.xlabel("Rok")
plt.ylabel("Ilosc")

plt.suptitle("Liczba urodzonych K i M")

plt.show()
