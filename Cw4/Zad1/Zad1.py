lista = []
for x in range(1,100):
    if x % 4 == 0:
        lista.append(x)

plik = open("Zad1_plik.txt", "w")

plik.writelines(str(lista))

plik.close()

