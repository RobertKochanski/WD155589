import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")

srednia = df[df["Data zamowienia"].str.contains("2004")]["Utarg"].mean()

print(srednia)
