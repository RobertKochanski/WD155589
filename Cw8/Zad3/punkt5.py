import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")

suma = df[(df["Kraj"] == "Polska") & df["Data zamowienia"].str.contains("2005")]["idZamowienia"].count()

print(suma)
