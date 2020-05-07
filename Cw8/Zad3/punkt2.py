import pandas as pd

df = pd.read_csv("zamowienia.csv", sep=";")

naj = df.nlargest(5, ["Utarg"])

print(naj)
