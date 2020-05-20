import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import random as r


plik = pd.read_csv("zamowienia.csv", sep=";")

dane = plik.groupby("Sprzedawca")["Utarg"].sum().reset_index()

explode = [0 for i in range(len(dane["Sprzedawca"]))]
explode[r.randint(0, len(dane["Sprzedawca"]) - 1)] = 0.2

wedges, texts, autotexts = plt.pie(dane["Utarg"], labels=dane["Sprzedawca"],
                                   autopct=lambda pct: "{:.2f}%".format(pct), textprops=dict(color="black"), shadow=True, explode=explode)
plt.setp(autotexts, size=14, weight="bold")
plt.title("Procentowy Udzial Sprzedawcow")
plt.legend(title='Sprzedawcy', loc="upper left", bbox_to_anchor=(-0.4, 1))
plt.show()
