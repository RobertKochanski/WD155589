import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")

plik1 = df[df["Data zamowienia"].str.contains("2004")].to_csv("zamowienia_2004.csv")
plik2 = df[df["Data zamowienia"].str.contains("2005")].to_csv("zamowienia_2005.csv")

