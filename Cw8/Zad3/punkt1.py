import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")

unique = df["Sprzedawca"].unique()

print(unique)