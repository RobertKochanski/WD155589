import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")

suma = df.groupby(["Kraj"])["idZamowienia"].count()

print(suma)
