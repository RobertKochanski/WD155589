import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")

ilosc = df.groupby(["Sprzedawca"])["idZamowienia"].count()

print(ilosc)
