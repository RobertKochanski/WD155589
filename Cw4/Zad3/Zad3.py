with open("Zad3.txt", "w") as plik:
    plik.writelines("asdfasgafgsdfg\nasdfasgdfgsdfasdfsa\ngfdsgcv\nbfds\nsdfb\nb\ndsfgregfsgdfg")

with open("Zad3.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")