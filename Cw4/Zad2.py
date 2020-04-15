sciezka = ("Zad1\Zad1_plik.txt")

plik = open(sciezka, "r")
dane = plik.readline()
plik.close()

print(dane)